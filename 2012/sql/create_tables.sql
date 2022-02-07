CREATE TABLE voters_2012 (
    voter_id                        varchar,
    voter_name                      varchar,
    voter_name_searchable           varchar,
    poll_category                   varchar,
    voter_role                      varchar,
    voter_title                     varchar,
    voter_nationality               varchar,
    voter_gener                     varchar,
    film_count                      integer,
    voter_comments                  varchar
);

\copy voters_2012 FROM '~/Desktop/voters_2012.csv' DELIMITER ',' CSV;

CREATE TABLE votes_2012 (
    voter_id                        varchar,
    raw_film_title                  varchar,
    normed_film_title               varchar,
    searchable_film_title           varchar,
    film_director                   varchar,
    film_director_searchable        varchar,
    film_year                       integer,
    film_id                         varchar
);

\copy votes_2012 FROM '~/Desktop/votes_2012.csv' DELIMITER ',' CSV;

CREATE TABLE films_2012 (
    film_id                         varchar,
    title_raw                       varchar,
    title_searchable                varchar,
    director_raw                    varchar,
    director_searchable             varchar,
    year                            integer,
    country                         varchar,
    genre                           varchar,
    media_type                      varchar,
    content_type                    varchar,
    actors_raw                      varchar,
    actors_searchable               varchar,
    alternate_titles_raw            varchar,
    alternate_titles_searchable     varchar
);

\copy films_2012 FROM '~/Desktop/films_2012.csv' DELIMITER ',' CSV;
