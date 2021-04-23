from db.run_sql import sql
from models.team import Team
from models.player import Player
from models.game import Game

def save(team):
    sql = "INSERT INTO teams (name, sponsor) VALUES (%s, %s) RETURNING id"
    values = [team.name, team.sponsor]
    results = run_sql(sql, values)
    id = results[0]['id'
    zombie.id = id]