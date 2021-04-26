import pdb

from models.team import Team
import repositories.team_repository as team_repository

from models.player import Player
import repositories.player_repository as player_repository

from models.game import Game
import repositories.game_repository as game_repository

team_repository.delete_all()
player_repository.delete_all()
game_repository.delete_all()


team_1 = Team("Grange", "Nike")
team_repository.save(team_1)
team_2 = Team("Inverleith", "Adidas")
team_repository.save(team_2)
team_3 = Team("Kelburn", "Puma")
team_repository.save(team_3)

player_1 = Player("Kieran Lamb", "Centre Back", team_1)
player_repository.save(player_1)

player_2 = Player("Aidan Lamb", "Left back", team_2)
player_repository.save(player_2)

player_3 = Player("Gwen", "Centre mid", team_1)
player_repository.save(player_3)

player_4 = Player("Stuart", "GK", team_1)
player_repository.save(player_4)

game_1 = Game("12/07/95", "Peffermill", team_1, team_2, 1, 1)
game_repository.save(game_1)

game_2 = Game("25/12/2020", "Inveralmond", team_3, team_1, 2, 0)
game_repository.save(game_2)

game_3 = Game("4/03/2008", "Glasgow Green", team_2, team_1, 2, 4)
game_repository.save(game_3)

# game_4 = Game("20/06/2012", "Aberdeen", team_2, team_3, 10, 4)
# game_repository.save(game_4)



# team_repository.games(team_1)



pdb.set_trace()


# game_4.date = "0000000"
# game_4.venue = "test"
# game_4.team_1_score = 1
# game_repository.update(game_4)


# game_repository.select_all()

# game_repository.select(21)

# game_repository.delete(25)


# player_repository.select_all()

# team_repository.players(team_1)

# player_repository.select(10)

# player_repository.delete(12)

# player_1.name = "Gwen"
# player_repository.update(player_1)

# team_repository.select(87)

# team_repository.select_all()

# team_repository.delete(88)

# team_3.name = "Grangess"
# team_repository.update(team_3)

