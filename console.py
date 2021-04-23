import pdb

from models.team import Team
import repositories.team_repository as team_repository

team_repository.delete_all()

team_1 = Team("Grange", "Nike")
team_repository.save(team_1)
team_2 = Team("Inverleith", "Adidas")
team_repository.save(team_2)
team_3 = Team("Kelburn", "Puma")
team_repository.save(team_3)


# team_repository.select(23)

team_repository.select_all()