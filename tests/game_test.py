import unittest
from models.game import Game
from models.team import Team

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game("12/07/2021", "Peffermill", 1, 2, 1, 1,)
        self.team_1 = Team("Grange", "Nike")
        self.team_2 = Team("Edinburgh Uni", "Addias")


    def test_game_has_date(self):
        self.assertEqual("12/07/2021", self.game.date)

    def test_game_has_venue(self):
        self.assertEqual("Peffermill", self.game.venue)

    def test_game_has_team_1(self):
        self.assertEqual(1, self.game.team_1)

    