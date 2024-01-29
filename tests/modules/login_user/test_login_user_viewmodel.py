from src.modules.login_user.app.login_user_viewmodel import LoginUserViewmodel, UserViewmodel
from src.shared.domain.entities.user import User


class Test_LoginUserViewmodel:
    def test_login_user_viewmodel(self):
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

        login_user_viewmodel = LoginUserViewmodel(data)

        expected = {
            'user': {
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
            },
            'message': 'Login realizado com sucesso!',
        }

        assert login_user_viewmodel.to_dict() == expected

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


