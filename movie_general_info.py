import requests
import pandas as pd


def read_dict(ls, typing):
    new_ls = [value.get(typing) for value in ls]
    string = ', '.join(new_ls)
    return string


if __name__ == '__main__':
    header = {"x-api-key": '',
              'Content-Type': 'application/json'}
    df = pd.DataFrame(data=None, columns=['kinopoiskId', 'nameOriginal', 'nameRu', 'ratingGoodReview',
                                          'ratingKinopoisk', 'ratingImdb', 'ratingFilmCritics', 'ratingRfCritics',
                                          'year', 'ratingAgeLimits', 'genres', 'countries', 'slogan', 'description',
                                          'shortDescription'])
    df_idx = pd.read_csv('data/all_movie_id.csv')

    for scrapingId in range(len(df_idx)):
        movie_id = df_idx.loc[scrapingId]['Movie_id']
        reqs = requests.get(f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{movie_id}', headers=header)
        content = reqs.json()

        genres = read_dict(content.get('genres'), 'genre')
        countries = read_dict(content.get('countries'), 'country')
        df.loc[len(df)] = [movie_id, content.get('nameOriginal'), content.get('nameRu'), content.get('ratingGoodReview'),
                           content.get('ratingKinopoisk'), content.get('ratingImdb'), content.get('ratingFilmCritics'),
                           content.get('ratingRfCritics'), content.get('year'), content.get('ratingAgeLimits'), genres,
                           countries, content.get('slogan'), content.get('description'), content.get('shortDescription')]
        print(f'Movie processed: {scrapingId+1}/{len(df_idx)}')

    df.to_csv(f'data/movies_info.csv', index=False)
