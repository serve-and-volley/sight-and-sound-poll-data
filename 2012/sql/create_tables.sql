CREATE TABLE voters_2012 (
    voter_id            varchar,    
    voter_name          varchar,
    voter_url           varchar,
    voter_role          varchar,
    voter_nationality   varchar,
    voter_gender        varchar,
    poll_category       varchar,
    voter_title         varchar,
    film_count          integer,
    voter_comments      varchar
);

\copy voters_2012 FROM '~/Desktop/voters_2012.csv' DELIMITER ',' CSV;

CREATE TABLE votes_2012 (
    voter_id            varchar,
    votes_film_title    varchar,
    film_url            varchar,
    film_id             varchar,
    film_year           integer,
    film_director       varchar
);

\copy votes_2012 FROM '~/Desktop/votes_2012.csv' DELIMITER ',' CSV;

CREATE TABLE films_2012 (
    film_id             varchar,    
    films_film_title    varchar,
    director            varchar,
    year                integer,
    country             varchar,
    genre               varchar,
    film_type           varchar,
    category            varchar,
    actors              varchar,
    alternate_titles    varchar
);

\copy films_2012 FROM '~/Desktop/films_2012.csv' DELIMITER ',' CSV;
