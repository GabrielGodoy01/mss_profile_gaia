from src.modules.get_all_users.app.get_all_users_viewmodel import GetAllUsersViewmodel, UserViewmodel
from src.shared.domain.entities.user import User
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetAllUsersViewmodel:
    def test_get_all_users_viewmodel(self):
        data = User(
            user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e123',
            email='v1zg0@example.com',
            name='Gabriel',
            department='INTELICITY',
            role_dashboards=True,
            role_fiscalizacao=True,
            role_geoinfra=True,
            role_drenagem=True,
            role_usuarios=True,
            role_tickets=True,
            role_cadastro_obra=True,
            role_selimp=True,
            role_compat=True,
            enabled=True,
        )
        
        viewmodel = GetAllUsersViewmodel([data])

        expected = {
            'user_list': [
                    {
                        'user_id': 'e73626b5-462d-4a3f-bef5-ae7cbb45e123',
                        'email': 'v1zg0@example.com',
                        'name': 'Gabriel',
                        'enabled': True,
                        'department': 'INTELICITY',
                        'role_dashboards': True,
                        'role_fiscalizacao': True,
                        'role_geoinfra': True,
                        'role_drenagem': True,
                        'role_usuarios': True,
                        'role_tickets': True,
                        'role_cadastro_obra': True,
                        'role_selimp': True,
                        'role_compat': True,
                    }
                ],
            'message': 'Usuários retornados com sucesso!'
        }

        assert viewmodel.to_dict() == expected
    
    def test_user_viewmodel(self):
        viewmodel = UserViewmodel(
            user=User(
            user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e123',
            email='v1zg0@example.com',
            name='Gabriel',
            department='INTELICITY',
            role_dashboards=True,
            role_fiscalizacao=True,
            role_geoinfra=True,
            role_drenagem=True,
            role_usuarios=True,
            role_tickets=True,
            role_cadastro_obra=True,
            role_selimp=True,
            role_compat=True,
            enabled=True,
        )
        )

        response = viewmodel.to_dict()

        data = {
            'user_id': 'e73626b5-462d-4a3f-bef5-ae7cbb45e123',
            'email': 'v1zg0@example.com',
            'name': 'Gabriel',
            'department': 'INTELICITY',
            'role_dashboards': True,
            'role_fiscalizacao': True,
            'role_geoinfra': True,
            'role_drenagem': True,
            'role_usuarios': True,
            'role_tickets': True,
            'role_cadastro_obra': True,
            'role_selimp': True,
            'role_compat': True,
            'enabled': True,
        }
    
        assert response == data