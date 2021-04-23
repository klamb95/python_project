import unittest
from models.player import Player
from models.team import Team

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Kieran Lamb", "Centre Back", 1 )
        self.team = Team("Inverleith", "Addias")

    
    def test_player_has_name(self):
        self.assertEqual("Kieran Lamb", self.player.name)
        
