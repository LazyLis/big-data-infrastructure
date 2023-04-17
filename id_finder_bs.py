import requests
from bs4 import BeautifulSoup as BS
import pandas as pd

if __name__ == '__main__':
    header = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/111.0.0.0 Safari/537.36',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/'
                        'apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'}

    proxy = {
        # "https": 'http://176.196.250.86:3128',
        "http": 'http://109.206.139.125:3128'
    }
    # [{'http': p} for p in proxies]; proxies = ['176.196.250.86:3128', '109.206.139.125:3128']
    num_page = 0 # up to 13
    reqs = requests.get('https://www.kinopoisk.ru/top/navigator/m_act[egenre]/1750%2C15%2C14%2C28%2C25%2C999%'
                        '2C26%2C1751/m_act[years]/2000%3A/m_act[budget]/10%3A/m_act[is_film]/on/order/rating/page/1'
                        '/#results',
                        headers=header, proxies=proxy)
    movie_ids = []
    if reqs.status_code == 200:
        page = BS(reqs.text, "html.parser")

        all_movie_info = page.find_all('div', attrs={'data-from': "kp"})
        for films_info in all_movie_info:
            movie_id = films_info.attrs.get('data-kp-film-id')
            movie_ids.append(movie_id)
        df = pd.DataFrame(data=movie_ids, columns=['Movie_id'])
        df.to_csv(f'data/page{num_page}.csv')
