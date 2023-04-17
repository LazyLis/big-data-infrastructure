import requests
import pandas as pd


if __name__ == '__main__':
    header = {"x-api-key": 'H8B6W6G-1X5422R-M072R8K-2XANQ44',
              'Content-Type': 'application/json'}
    num_page_last = 15

    movie_ids = []
    for num_page in range(1, num_page_last+1):
        reqs = requests.get(f'https://api.kinopoisk.dev/v1/movie?selectFields=id%20name&page={num_page}&limit=200&year=2000-2023'
                            '&rating.kp=6.0-10.0&budget.value=10000000-300000000&budget.currency=%24', headers=header)
        content = reqs.json()

        for movie_info in content.get('docs'):
            movie_id = movie_info.get('id')
            movie_ids.append(movie_id)

    df = pd.DataFrame(data=movie_ids, columns=['Movie_id'])
    df.to_csv(f'data/page_all_{num_page_last}.csv')
    print()