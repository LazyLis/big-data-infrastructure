import requests
import pandas as pd

if __name__ == '__main__':
    header = {"x-api-key": '',
              'Content-Type': 'application/json'}
    df = pd.DataFrame(data=None, columns=['kinopoiskId', 'reviewId', 'type', 'positiveRating', 'negativeRating', 'title',
                                          'description', 'scrapingId'])
    df_idx = pd.read_csv('data/all_movie_id.csv')

    for scrapingId in range(len(df_idx)):
        movie_id = df_idx.loc[scrapingId]['Movie_id']
        review_req = requests.get(
            f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{movie_id}/reviews?page=1&order=DATE_DESC', headers=header)
        content_rev = review_req.json()
        num_page_last = content_rev.get('totalPages')

        review_id = 1
        for num_page in range(1, num_page_last+1):
            review_req = requests.get(f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{movie_id}/reviews?page={num_page}&'
                                      f'order=DATE_DESC', headers=header)

            # total_rev = content_rev.get('total')
            # num_pos_rev = content_rev.get('totalPositiveReviews')
            # num_neg_rev = content_rev.get('totalNegativeReviews')
            # num_neu_rev = content_rev.get('totalNeutralReviews')

            for review in content_rev.get('items'):
                df.loc[len(df)] = [movie_id, review_id, review.get('type'), review.get('positiveRating'),
                                   review.get('negativeRating'), review.get('title'),
                                   review.get('description'), scrapingId]
                review_id += 1
        print(f'Movie processed: {scrapingId+1}/{len(df_idx)}')
        df.to_csv(f'data/review_info.csv', index=False)
