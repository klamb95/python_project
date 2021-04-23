from db.run_sql import run_sql
from models.player import Player
from models.team import Team

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