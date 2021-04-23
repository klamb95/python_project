from db.run_sql import run_sql
from models.player import Player
from models.team import Team

import repositories.team_repository as team_repository

def delete_all():
    sql = "DELETE FROM players "
    run_sql(sql)

def save(player):
    sql = "INSERT INTO players (name, position, team_id) VALUES (%s, %s, %s) RETURNING *"
    values = [player.name, player.position, player.team.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    player.id = id
    return player

def select_all():
    players = []

    sql = "SELECT * FROM players"
    results = run_sql(sql)
    for row in results:
        team = team_repository.select(row['team_id'])
        player = Player(row['name'], row['position'], team, row['id'])
        players.append(player)