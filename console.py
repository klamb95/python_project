import pdb

from models.team import Team
import repositories.team_repository as team_repository

team_repository.delete_all()

team_1 = Team("Grange", "Nike")
team_repository.save(team_1)

team_repository.select(23)