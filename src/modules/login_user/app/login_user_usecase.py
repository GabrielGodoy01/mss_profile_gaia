from src.shared.domain.entities.user import User
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, InvalidCredentials


class LoginUserUsecase:

    def __init__(self, repo: IUserRepository):
        self.repo = repo

    def __call__(self, user_id: str, name: str, email: str, groups: list) -> User:
        
        user = self.repo.get_user_by_id(user_id=user_id)

        if user is None:
            if "GAIA" in groups:
                user = User(user_id=user_id,name=name, email=email, enabled=True, department=None, role_dashboards=None, role_fiscalizacao=None, role_geoinfra=None, role_drenagem=None, role_usuarios=None, role_tickets=None, role_cadastro_obra=None, role_selimp=None, role_compat=None)
                return self.repo.create_profile(user=user)
            else:
                raise InvalidCredentials(message="Usuário não esta apto para o sistema")
        return user
