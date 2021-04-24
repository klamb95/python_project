from db.run_sql import run_sql
from models.team import Team

import repositories.team_repository as team_repository

def save(game):
    sql = "INSERT INTO games (date, venue, team_1_id, team_2_id, team_1_score, team_2_score) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [game.date, game.venue, game.team_1.id, game.team_2.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    game.id = id
    return game

    