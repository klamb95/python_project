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
    team_1_id INT REFERENCES teams(id) ON DELETE CASCADE,
    team_2_id INT REFERENCES teams(id) ON DELETE CASCADE,
    team_1_score INT,
    team_2_score INT
   
);

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    team_id SERIAL REFERENCES teams(id) ON DELETE CASCADE,
    position VARCHAR(255)
)

INSERT INTO teams (name, sponsor) VALUES ('Grange', 'Nike');
INSERT INTO teams (name, sponsor) VALUES ('Kelburn', 'addias');
INSERT INTO teams (name, sponsor) VALUES ('Edinburgh Uni', 'puma');
INSERT INTO teams (name, sponsor) VALUES ('Inverleith', 'test');

INSERT INTO games (date, venue, team_1_id, team_2_id, team_1_score, team_2_score) VALUES ('23/07/95', 'CALA', 1, 2, 1, 1);
INSERT INTO games (date, venue, team_1_id, team_2_id, team_1_score, team_2_score) VALUES ('24/07/95', 'murryfeild', 3, 4, 2, 2);
INSERT INTO games (date, venue, team_1_id, team_2_id, team_1_score, team_2_score) VALUES ('25/07/95', 'park', 1, 3, 3, 3);
INSERT INTO games (date, venue, team_1_id, team_2_id, team_1_score, team_2_score) VALUES ('26/07/95', 'test', 1, 2, 2, 2);
INSERT INTO games (date, venue, team_1_id, team_2_id, team_1_score, team_2_score) VALUES ('27/07/95', 'livi', 1, 4, 2, 1);
INSERT INTO games (date, venue, team_1_id, team_2_id, team_1_score, team_2_score) VALUES ('28/07/95', 'glasgow', 2, 3, 1, 1);
INSERT INTO games (date, venue, team_1_id, team_2_id, team_1_score, team_2_score) VALUES ('28/07/95', 'highland', 4, 1, 1, 1);







-- CREATE TABLE examples (
--     id SERIAL PRIMARY KEY,
--     team_1_id INT REFERENCES teams(id) ON DELETE CASCADE,
--     team_2_id INT REFERENCES teams(id) ON DELETE CASCADE,
--     game_id INT REFERENCES games(id) ON DELETE CASCADE
-- );
