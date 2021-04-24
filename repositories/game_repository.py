from db.run_sql import run_sql
from models.team import Team
from models.game import Game

import repositories.team_repository as team_repository

def delete_all():
    sql = "DELETE FROM games"
    run_sql(sql)

def save(game):
    sql = "INSERT INTO games (date, venue, team_1_id, team_2_id, team_1_score, team_2_score) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [game.date, game.venue, game.team_1.id, game.team_2.id, game.team_1_score, game.team_2_score]
    results = run_sql(sql, values)
    id = results[0]['id']
    game.id = id
    return game

def select_all():
    games = []

    sql = "SELECT * FROM games"
    results = run_sql(sql)
    for row in results:
        team_1 = team_repository.select(row['team_1_id'])
        team_2 = team_repository.select(row['team_2_id'])
        game = Game(row['date'], row['venue'], team_1, team_2, row['team_1_score'], row['team_2_score'], row['id'])
        games.append(game)
    return games

def select(id):
    game = None

    sql = "SELECT * FROM games WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        team_1 = team_repository.select(result['team_1_id'])
        team_2 = team_repository.select(result['team_2_id'])
        game = Game(result['date'], result['venue'], team_1, team_2, result['team_1_score'], result['team_2_score'], result['id'])
    return game

# SELECT * FROM games WHERE team_1_id = 34 OR team_2_id = 34

