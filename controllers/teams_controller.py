from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import team_repository
from models.team import Team

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

@teams_blueprint.route("/teams/new")
def new_team():
    return render_template("teams/new.html")

@teams_blueprint.route("/teams", methods=["POST"])
def create_team():
    name = request.form["name"]
    sponsor = request.form["sponsor"]
    new_team = Team(name, sponsor)
    team_repository.save(new_team)
    return redirect("/teams")

@teams_blueprint.route("/teams/<id>/delete", methods=['POST'])
def delete_team(id):
    team_repository.delete(id)
    return redirect('/teams')

@teams_blueprint.route("/teams/<id>/edit")
def edit_team(id):
    team = team_repository.select(id)
    return render_template("teams/edit.html", team = team)


@teams_blueprint.route("/teams/<id>", methods=['POST'])
def update_team(id):
    name = request.form["name"]
    sponsor = request.form["sponsor"]
    team = Team(name, sponsor, id)
    team_repository.update(team)
    return redirect("/teams")

