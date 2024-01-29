

from typing import List
from src.shared.domain.entities.user import User
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound


class GetAllUsersUsecase:
    def __init__(self, repo: IUserRepository):
        self.repo = repo
    
    def __call__(self, user_id: str) -> List[User]:

        user = self.repo.get_user_by_id(user_id=user_id)

        if user is None:
            raise NoItemsFound("user_id não encontrado")
                
        if user.department != 'ADMINISTRADOR' and user.department != 'INTELICITY':
            raise ForbiddenAction("Usuário não é Administrador")
        
        all_users = self.repo.get_all_users()

        if not all_users:
            raise NoItemsFound("Nenhum usuário cadastrado encontrado")
        
        return all_users