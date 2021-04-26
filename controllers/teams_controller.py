from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import team_repository

teams_blueprint = Blueprint("teams", __name__)

@teams_blueprint.route("/teams")
def teams():
    teams = team_repository.select_all()
    return render_template("teams/index.html", teams = teams)

# @teams_blueprint.route("/teams/<id>")
# def show_team(id):
#     # players = team_repository.players(id)
#     games = team_repository.games(id)
#     team_1_name = team_repository.select(games.team_1)['name']
#     team_2_name = team_repository.select(games.team_2)['name']
#     games.team_1 = team_1_name
#     games.team_2 = team_2_name
#     return render_template("teams/show.html",games=games, team_1 = team_1, team_2 = team_2)


@teams_blueprint.route("/teams/<id>")
def show_team(id):
    games = team_repository.games(id)
    team = team_repository.select(id)
    return render_template("teams/show.html", games=games, team=team)

@teams_blueprint.route("/teams/new")
def new_team():
    return render_template("teams/new.html")

@zombies_blueprint.route("/teams", methods=["POST"])
def create_team():
    name = request.form("name")
    sponsor = request.form("sponsor")
    new_team = Team(name, sponsor)
    team_repository.save(new_team)
    return redirect("/teams")
    