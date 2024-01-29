from src.shared.domain.entities.user import User
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound


class UpdateUserUsecase:
    
    def __init__(self, repo: IUserRepository):
        self.repo = repo

    def __call__(self, new_user_data: User) -> User:
        
        user = self.repo.get_user_by_id(user_id=new_user_data.user_id)

        if user is None:
            raise NoItemsFound("user")
                
        if user.department != 'ADMINISTRADOR' and user.department != 'INTELICITY':
            raise ForbiddenAction("Usuário não é Administrador")
        
        user = self.repo.update_user_by_id(new_user_data=new_user_data)
        return user