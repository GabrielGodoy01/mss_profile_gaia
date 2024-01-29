from typing import List, Optional
from src.shared.domain.entities.user import User
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound


class UserRepositoryMock(IUserRepository):

    users: List[User]

    def __init__(self):
        self.users_list = [
             User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45e123", email="gabriel.godoybz@hotmail.com", name='Gabriel', role_cadastro_obra=True, role_compat=True, role_dashboards=True, role_drenagem=True, role_fiscalizacao=True, role_geoinfra=True, role_selimp=True, role_usuarios=True, role_tickets=True, enabled=True, department='INTELICITY'),
             User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45e456", email="gabriel.godoybz@gmail.com", name='Gabriel', department='CONVIAS', enabled=True,),
        ]
    
    def get_user_by_id(self, user_id: str) -> Optional[User]:
        for user in self.users_list:
            if user_id == user.user_id:
                return user
        return None
    
    def get_all_users(self) -> List[User]:
        if len(self.users_list) > 0:
            return self.users_list
        else:
            return None
    
    def create_profile(self, user_id: str, name: str, email: str) -> User:
        user = User(user_id=user_id, name=name, email=email, enabled=True, department=None, role_dashboards=None, role_cadastro_obra=None, role_compat=None, role_drenagem=None, role_fiscalizacao=None, role_geoinfra=None, role_selimp=None, role_usuarios=None, role_tickets=None)
        self.users_list.append(user)
        return user
    
    def update_user_by_id(self, new_user_data: User) -> User:
        user_to_update = self.get_user_by_id(new_user_data.user_id)

        if user_to_update is None:
            return None

        if user_to_update.user_id == new_user_data.user_id:
            user_to_update.name = new_user_data.name
            user_to_update.enabled = new_user_data.enabled
            user_to_update.role_cadastro_obra = new_user_data.role_cadastro_obra
            user_to_update.role_compat = new_user_data.role_compat
            user_to_update.role_dashboards = new_user_data.role_dashboards
            user_to_update.role_drenagem = new_user_data.role_drenagem
            user_to_update.role_fiscalizacao = new_user_data.role_fiscalizacao
            user_to_update.role_geoinfra = new_user_data.role_geoinfra
            user_to_update.role_selimp = new_user_data.role_selimp
            user_to_update.role_tickets = new_user_data.role_tickets
            user_to_update.role_usuarios = new_user_data.role_usuarios
            user_to_update.department = new_user_data.department
            return user_to_update

    def check_user_group(self, user_id: str) -> bool:
        return True