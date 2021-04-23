import unittest
from models.player import Player
from models.team import Team

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Kieran Lamb", "Centre Back", 1 )
        self.team = Team("Inverleith", "Addias")

    
    def test_player_has_name(self):
        self.assertEqual("Kieran Lamb", self.player.name)

    def test_player_has_postion(self):
        self.assertEqual("Centre Back", self.player.position)

    def test_player_has_team(self):
        self.assertEqual(1, self.player.team)
