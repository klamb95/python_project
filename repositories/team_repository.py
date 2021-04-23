from db.run_sql import run_sql
from models.team import Team
from models.player import Player
from models.game import Game

def save(team):
    sql = "INSERT INTO teams (name, sponsor) VALUES (%s, %s) RETURNING id"
    values = [team.name, team.sponsor]
    results = run_sql(sql, values)
    id = results[0]['id']
    team.id = id

def delete_all():
    sql = "DELETE FROM teams"
    run_sql(sql)