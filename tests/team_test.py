import unittest
from models.team import Team

class TestTeam(unittest.TestCase):

    def setUp(self):
        self.team = Team("Grange", "Nike")

    
    def test_team_has_name(self):
        self.assertEqual("Grange", self.team.name)

    def test_team_has_sponsor(self):
        self.assertEqual("Nike", self.team.sponsor)