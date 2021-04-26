from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import team_repository
from models.team import Team
from models.game import Game

games_blueprint = Blueprint("games", __name__)

@games_route("/games")
def games():
    games = game_repository.select_all()
    return render_template("games/index.html", games = games)
