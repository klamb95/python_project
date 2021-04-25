from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import team_repository

teams_blueprint = Blueprint("teams", __name__)

@teams_blueprint.route("/teams")
def teams():
    teams = team_repository.select_all()
    return render_template("teams/index.html", teams = teams)

@teams_blueprint.route("/teams/<id>")
def show_team(id):
    # players = team_repository.players(id)
    games = team_repository.games(id)
    team = team_repository.select(id)
    return render_template("teams/show.html",games=games, team=team)

