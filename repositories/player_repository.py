from db.run_sql import import run_sql
from models.player import Player
from models.team import Team

def delete_all():
    sql = "DELETE FROM players "
    run_sql(sql)
    