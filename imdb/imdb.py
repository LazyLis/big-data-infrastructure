import json
import pandas as pd
import re
import requests
import logging
from pathlib import Path
from tqdm import tqdm
from time import sleep
from random import randint
from bs4 import BeautifulSoup


# Parsing params
PAGES_RANGE = range(6, 16)  # range(1, 6)

# Directories
SAVE_DIRECTORY = Path(r"C:\Users\petro\Desktop\IMDB_parsing")
SAVE_FILMS_JSON = SAVE_DIRECTORY.joinpath('films_data_2.json')
SAVE_REVIEWS_JSON = SAVE_DIRECTORY.joinpath('reviews_data_2.json')
SAVE_FILMS_CSV = SAVE_DIRECTORY.joinpath('films_data_2.csv')
SAVE_REVIEWS_CSV = SAVE_DIRECTORY.joinpath('reviews_data_2.csv')

# URLs
URL_MOVIES_PAGE_TEMPLATE = 'https://www.imdb.com/search/title/?title_type=feature&release_date=2000-01-01,&user_rating=6.0,&adult=include&start={starting_position}&ref_=adv_nxt&sort=num_votes,desc&count={count_per_page}'
API_URL = 'https://imdb-api.tprojects.workers.dev'
URL_MOVIE_API_TEMPLATE = API_URL + '/title/{title_id}'
URL_MOVIE_REVIEWS_API_TEMPLATE = API_URL + '/reviews/{title_id}?option=helpfulness&sortOrder=desc'

# Other web stuff
HEADERS_IMDB_WEB = {'User-Agent': 'Mozilla/5.0'}
IMDB_TITLE_PATTERN = r"/title/(tt\d+)/"


def wait():
    sleep(randint(1, 3))


def get_page_results(page_num):
    count_per_page = 250  # [50, 100, 250]
    starting_position = 1 + (page_num - 1) * count_per_page
    url = URL_MOVIES_PAGE_TEMPLATE.format(starting_position=starting_position, count_per_page=count_per_page)

    result_page = requests.get(url, headers=HEADERS_IMDB_WEB)
    # wait()

    if result_page.status_code != 200:
        logging.error(f'Results at {starting_position} (url: {url}): code {result_page.status_code}')
        return []

    soup = BeautifulSoup(result_page.text)
    page_results = soup.find_all(class_='lister-item mode-advanced')
    return page_results


def get_film_data(title_id):
    url = URL_MOVIE_API_TEMPLATE.format(title_id)
    result_film = requests.get(url)
    wait()
    if result_film.status_code != 200:
        logging.error(f'Results of the film {title_id}: code {result_film.status_code}')
        # continue
    film_data = result_film.json()
    if 'releaseDeatiled' in film_data:
        del film_data['releaseDeatiled']
    return film_data


def get_film_reviews_data(title_id, pages_num=3, film_reviews_data=None, url=None, current_page_num=1):
    if current_page_num > pages_num:
        return film_reviews_data

    if current_page_num == 0:
        film_reviews_data = []
        url = URL_MOVIE_REVIEWS_API_TEMPLATE.format(title_id)

    result = requests.get(url)
    if result.status_code != 200:
        logging.error(f'Results of the reviews page {current_page_num}, film {title_id}: code {result.status_code}')
        return film_reviews_data
    wait()
    data = result.json()
    film_reviews_data += data['reviews']
    next_url = f'{API_URL}{data["next_api_path"]}'
    film_reviews_data = get_film_reviews_data(title_id, film_reviews_data, next_url, current_page_num + 1)
    return film_reviews_data


def parse_pages(pages_range):
    films_data = []
    reviews_data = []
    i = 0  # counter
    title_id = None  # placeholder

    for page_num in tqdm(pages_range, 'pages'):
        page_results = get_page_results(page_num)
        for page_result in tqdm(page_results, f'films on page {page_num}'):
            i += 1
            try:
                is_match = re.search(IMDB_TITLE_PATTERN, page_result.find('a').get('href'))
                title_id = is_match.group(1)
                film_data = get_film_data(title_id)
                films_data.append(film_data)
                film_reviews_data = get_film_reviews_data(title_id)
                reviews_data += film_reviews_data
            except Exception as e:
                logging.error(f'film {title_id}')
                logging.exception(e)

            if i % 100 == 0:
                with open(SAVE_FILMS_JSON, 'w') as f:
                    json.dump(films_data, f)
                with open(SAVE_REVIEWS_JSON, 'w') as f:
                    json.dump(reviews_data, f)

    with open(SAVE_FILMS_JSON, 'w') as f:
        json.dump(films_data, f)
    with open(SAVE_REVIEWS_JSON, 'w') as f:
        json.dump(reviews_data, f)

    df_films = pd.json_normalize(films_data)
    df_reviews = pd.json_normalize(reviews_data)
    df_films.to_csv(SAVE_FILMS_CSV)
    df_reviews.to_csv(SAVE_REVIEWS_CSV)


if __name__ == '__main__':
    parse_pages(PAGES_RANGE)
