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

def select(id):
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    team = Team(result["name"], result["sponsor"], result["id"])
    return team

def select_all():
    teams = []
    sql = "SELECT * FROM teams"
    results = run_sql(sql)
    for result in results:
        team = Team(result["name"], result["sponsor"], result["id"])
        teams.append(team)
    return teams

def delete(id):
    sql = "DELETE FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(team):
    sql = "UPDATE teams SET (name, sponsor) = (%s, %s) WHERE id = %s"
    values = [team.name, team.sponsor, team.id]
    run_sql(sql, values)



def players(id):
    players = []

    sql = "SELECT * FROM players WHERE team_id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        player = Player(row['name'], row['position'], team, row['id'] )
        players.append(player)
    return players

def games(id):
    games = []
    sql = "SELECT * FROM games WHERE team_1_id = %s OR team_2_id = %s"
    values = [id, id]
    results = run_sql(sql, values)
  

    for row in results:
        team_1 = select(row['team_1_id'])
        team_2 = select(row['team_2_id'])
        game = Game(row['date'], row['venue'], team_1, team_2, row['team_1_score'], row['team_2_score'], row['id'])
        games.append(game)
    return games
    
     



