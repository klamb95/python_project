import pdb

from models.team import Team
import repositories.team_repository as team_repository

from models.player import Player
import repositories.player_repository as player_repository

team_repository.delete_all()
player_repository.delete_all()

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

player_repository.select_all()

# player_repository.select(10)

player_repository.delete(12)



# team_repository.select(87)

# team_repository.select_all()

# team_repository.delete(88)

# team_3.name = "Grangess"
# team_repository.update(team_3)

