import requests
import pandas as pd


if __name__ == '__main__':
    header = {"x-api-key": '',
              'Content-Type': 'application/json'}
    df = pd.DataFrame(data=None,
                      columns=['reviewsCount', 'lastSync'])

    df_idx = pd.read_csv('data/all_movie_id.csv')

    for scrapingId in range(len(df_idx)):
        movie_id = df_idx.loc[scrapingId]['Movie_id']
        reqs = requests.get(f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{movie_id}/reviews?'
                            f'page=1&order=DATE_DESC', headers=header)
        content = reqs.json()

        reqs_date = requests.get(f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{movie_id}', headers=header)
        content_update = reqs_date.json()
        last_update = content_update.get('lastSync')

        df.loc[len(df)] = [content.get('total'), last_update.split('T')[0]]
        print(f'Movie processed: {scrapingId+1}/{len(df_idx)}')
    df.to_csv(f'data/state_info.csv', index=False)
