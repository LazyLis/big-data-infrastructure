# Trivia

This chapter describes films & reviews data parsed from IMDB database for Big Data Infrastructure course project.

All the parsed data is available [via the link](https://drive.google.com/drive/folders/1_ejWt3Cqclk1pBfitTWgj42S3bjaytsq?usp=share_link) in `.csv` format.

# Data collection

The data was parsed from [imdb.com]() database.

## Filtering the films

List of films was taken directly from the website's [advanced title search](https://www.imdb.com/search/title/).
The search criteria:

- `title_type=feature` (films, not series)
- `release_date=2000-01-01` (just the 3rd millennium)
- `adult=include` (include R18 films)
- `sort=num_votes` (the most frequently rated films go first)

By the following rules, 15 pages of 250 films were taken (3750 entities).

## Films & reviews data retrieval

Films & reviews data were taken from an [unofficial user-made IMDB API](https://github.com/tuhinpal/imdb-api).

For each film, was taken the 100 most "useful" reviews (4 pages per 25).


# Data fields (WIP)

## Film fields (WIP)

| field                                   | description                                 |
|-----------------------------------------|---------------------------------------------|
| id                                      | the imdb.com technical title id             |
| review_api_path                         | path to reviews in the API (not used)       |
| imdb                                    | link to the title page on imdb.com          |
| contentType                             | E.g. "Movie"                                |
| productionStatus                        | E.g. "Released"                             |
| title                                   | The movie title in English                  |
| image                                   | Link to the main movie poster image         |
| images                                  | Link to several images related to the movie |
| plot                                    | Verbal plot annotation.                     |
| contentRating                           | PG-...                                      |
| genre                                   |                                             |
| year                                    |                                             |
| spokenLanguages                         |                                             |
| filmingLocations                        |                                             |
| runtime                                 |                                             |
| runtimeSeconds                          |                                             |
| actors                                  |                                             |
| directors                               |                                             |
| top_credits                             |                                             |
| rating.count                            |                                             |
| rating.star                             |                                             |
| award.wins                              |                                             |
| award.nominations                       |                                             |
| releaseDetailed.day                     |                                             |
| releaseDetailed.month                   |                                             |
| releaseDetailed.year                    |                                             |
| releaseDetailed.releaseLocation.country |                                             |
| releaseDetailed.releaseLocation.cca2    |                                             |
| releaseDetailed.originLocations         |                                             |

## Review fields (WIP)
