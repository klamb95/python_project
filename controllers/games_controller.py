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
    return render_template("games/show.html", game)

@games_blueprint.route("/games/new")
def new_game():
    return render_template("games/new.html")