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

| field                                   | type                       | description                                                               |
|-----------------------------------------|----------------------------|---------------------------------------------------------------------------|
| id                                      | str                        | Technical title id at imdb.com                                            |
| review_api_path                         | str                        | Path to reviews in the API (not used)                                     |
| imdb                                    | str                        | Link to the title page on imdb.com                                        |
| contentType                             | str                        | Mostly "Movie"                                                            |
| productionStatus                        | str                        | Mostly "Released"                                                         |
| title                                   | str                        | The movie title in English                                                |
| image                                   | str                        | Link to the main movie poster image                                       |
| images                                  | list[str]                  | Link to several images related to the movie                               |
| plot                                    | str                        | Verbal plot annotation.                                                   |
| contentRating                           | str                        | "PG-13", "R", etc.                                                        |
| genre                                   | list[str]                  | List of the movie genres.                                                 |
| year                                    | int                        | Release year.                                                             |
| spokenLanguages                         | list[dict[str, str]]       | List of spoken languages in the film.                                     |
| filmingLocations                        | list[str]                  | List of location names where the movie was filmed.                        |
| runtime                                 | str                        | Duration in the format "_h __m".                                          |
| runtimeSeconds                          | int                        | Duration in integer seconds.                                              |
| actors                                  | list[str]                  | List of main actor names.                                                 |
| directors                               | list[str]                  | List of director names.                                                   |
| top_credits                             | list[dict[str, list[str]]] | List of featured celebrities by categories: "Director", "Writer", "Star". |
| rating.count                            | int                        | Amount of rating evaluations (int).                                       |
| rating.star                             | float                      | Rating in stars 0-10 (float).                                             |
| award.wins                              | int                        | Amount of award wins (int).                                               |
| award.nominations                       | int                        | Amount of award nominations (int).                                        |
| releaseDetailed.day                     | float                      | Release day (float (???)).                                                |
| releaseDetailed.month                   | int                        | Release month (int).                                                      |
| releaseDetailed.year                    | int                        | Release year (int).                                                       |
| releaseDetailed.releaseLocation.country | str                        | Name of release country.                                                  |
| releaseDetailed.releaseLocation.cca2    | str                        | Code of release country.                                                  |
| releaseDetailed.originLocations         | list[dict[str, str]]       | Several countries (?).                                                    |

## Review fields

| field                                | type             | description                                                                                                                                                                                  |
|--------------------------------------|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| title_id                             | str              | Technical title id of the corresponding movie at imdb.com.                                                                                                                                   |
| id                                   | str              | Technical review id at imdb.com.                                                                                                                                                             |
| author                               | str              | Nickname of reviewer.                                                                                                                                                                        |
| authorUrl                            | str              | Link to the reviewer profile.                                                                                                                                                                |
| user_api_path                        | str              | Link to user via the API.                                                                                                                                                                    |
| date                                 | date (ISO) / str | Review date.                                                                                                                                                                                 |
| stars                                | int              | Score of the film by the reviewer.                                                                                                                                                           |
| heading                              | str              | Review heading.                                                                                                                                                                              |
| content                              | str              | Review text.                                                                                                                                                                                 |
| reviewLink                           | str              | Review link at imdb.com.                                                                                                                                                                     |
| helpfulNess.votes                    | int              | Number of all votes for helpfulness (positive plus negative).<br/>Be careful, sometimes wrongly equals to `1`.                                                                               |
| helpfulNess.votedAsHelpful           | int              | Number of positive votes for helpfulness.                                                                                                                                                    |
| helpfulNess.votedAsHelpfulPercentage | int              | Percentage of positive votes for helpfulness.<br/>Be careful, if `helpfulNess.votes` equals to `1`, the percentage is `helpfulNess.votedAsHelpful * 100`, which is obviously more than 100%. |

