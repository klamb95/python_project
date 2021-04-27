from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import team_repository
from repositories import game_repository
from models.team import Team
from models.game import Game
import pdb

games_blueprint = Blueprint("games", __name__)

@games_blueprint.route("/games")
def games():
    games = game_repository.select_all()
    return render_template("games/index.html", games = games)


@games_blueprint.route("/games/<id>")
def show_game(id):
    game = game_repository.select(id)
    return render_template("games/show.html", game=game)

@games_blueprint.route("/games/new")
def new_game():
    teams = team_repository.select_all()
    return render_template("games/new.html", teams = teams)

@games_blueprint.route("/games", methods = ["POST"])
def create_game():
    date = request.form["date"]
    venue = request.form["venue"]
    team_1_id = request.form["team_1_id"]
    team_1 = team_repository.select(team_1_id)
    team_2_id = request.form["team_2_id"]
    team_2 = team_repository.select(team_2_id)
    team_1_score = request.form["team_1_score"]
    team_2_score = request.form["team_2_score"]
    new_game = Game(date, venue, team_1, team_2, team_1_score, team_2_score)
    game_repository.save(new_game)
    return redirect('/games')

@games_blueprint.route("/games/<id>/delete", methods=['POST'])
def delete_game(id):
    game_repository.delete(id)
    return redirect('/games')

@games_blueprint.route("/games/<id>/edit")
def edit_game(id):
    teams = team_repository.select_all()
    game = game_repository.select(id)
    # team_1 = game.team_1
    # team_2 = game.team_2
    return render_template("games/edit.html", game = game, teams = teams)

@games_blueprint.route("/games/<id>", methods=['POST'])
def update_game(id):
    date = request.form["date"]
    venue = request.form["venue"]
    team_1_id = request.form["team_1_id"]
    team_1 = team_repository.select(team_1_id)
    team_2_id = request.form["team_2_id"]
    team_2 = team_repository.select(team_2_id)
    team_1_score = request.form["team_1_score"]
    team_2_score = request.form["team_2_score"]
    game = Game(date, venue, team_1, team_2, team_1_score, team_2_score, id)
    game_repository.update(game)
    return redirect("/games")

