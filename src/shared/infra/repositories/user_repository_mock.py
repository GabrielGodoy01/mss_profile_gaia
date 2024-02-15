from typing import List, Optional
from src.shared.domain.entities.user import User
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound


class UserRepositoryMock(IUserRepository):

    users: List[User]

    def __init__(self):
        self.users_list = [
             User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45e123", email="gabriel@hotmail.com", name='Gabriel', enabled=True, department='INTELICITY', role_dashboard_qualidade=True, role_dashboard_deteccao=True, role_dashboard_tempo=True, role_dashboard_geoinfra=True, role_dashboard_recapeamento=True, role_dashboard_anel_viario=True, role_dashboard_sist_unificado=True, role_modfisc_convias=True, role_modfisc_osmv=True, role_modfisc_osct=True, role_modfisc_relatoriomv=True, role_modfisc_vistoriapv=True, role_modfisc_vistoriarecape=True, role_interf_mapa=True, role_interf_protproc=True, role_drenagem_ativos=True, role_drenagem_redes=True, role_usuarios=True, role_tickets=True),
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
    
    def create_profile(self, user: User) -> User:
        self.users_list.append(user)
        return user
    
    def update_user_by_id(self, new_user_data: User) -> User:
        user_to_update = self.get_user_by_id(new_user_data.user_id)

        if user_to_update is None:
            return None

        if user_to_update.user_id == new_user_data.user_id:
            user_to_update.name = new_user_data.name
            user_to_update.enabled = new_user_data.enabled
            user_to_update.department = new_user_data.department
            user_to_update.role_dashboard_qualidade = new_user_data.role_dashboard_qualidade
            user_to_update.role_dashboard_deteccao = new_user_data.role_dashboard_deteccao
            user_to_update.role_dashboard_tempo = new_user_data.role_dashboard_tempo
            user_to_update.role_dashboard_geoinfra = new_user_data.role_dashboard_geoinfra
            user_to_update.role_dashboard_recapeamento = new_user_data.role_dashboard_recapeamento
            user_to_update.role_dashboard_anel_viario = new_user_data.role_dashboard_anel_viario
            user_to_update.role_dashboard_sist_unificado = new_user_data.role_dashboard_sist_unificado
            user_to_update.role_modfisc_convias = new_user_data.role_modfisc_convias
            user_to_update.role_modfisc_osmv = new_user_data.role_modfisc_osmv
            user_to_update.role_modfisc_osct = new_user_data.role_modfisc_osct
            user_to_update.role_modfisc_relatoriomv = new_user_data.role_modfisc_relatoriomv
            user_to_update.role_modfisc_vistoriapv = new_user_data.role_modfisc_vistoriapv
            user_to_update.role_modfisc_vistoriarecape = new_user_data.role_modfisc_vistoriarecape
            user_to_update.role_interf_mapa = new_user_data.role_interf_mapa
            user_to_update.role_interf_protproc = new_user_data.role_interf_protproc
            user_to_update.role_drenagem_ativos = new_user_data.role_drenagem_ativos
            user_to_update.role_drenagem_redes = new_user_data.role_drenagem_redes
            user_to_update.role_usuarios = new_user_data.role_usuarios
            user_to_update.role_tickets = new_user_data.role_tickets
            return user_to_update