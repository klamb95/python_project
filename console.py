import pdb

from models.team import Team
import repositories.team_repository as team_repository

team_repository.delete_all()

team1 = Team("Grange", "Nike")
team_repository.save(team1)
team2 = Team("Inverleith", "Adidas")
team_repository.save(team2)
team3 = Team("Kelburn", "Puma")
team_repository.save(team3)


# team_repository.select(23)

# team_repository.select_all()

# team_repository.delete(30)

# team3.name = "Grangess"
# team_repository.update(team3)

