DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS players;

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    sponsor VARCHAR(255)
);

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    date VARCHAR(255),
    venue VARCHAR(255),
    team_1_id SERIAL REFERENCES teams(id),
    team_2_id SERIAL REFERENCES teams(id),
    team_1_score INT,
    team_2_score INT
);

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    team_id SERIAL REFERENCES teams(id),
    position VARCHAR(255)
)