from src.modules.update_user.app.update_user_usecase import UpdateUserUsecase
from src.modules.update_user.app.update_user_controller import UpdateUserController
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_UpdateUserController:

    def test_update_user_controller(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': repo.users_list[0].email,
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboards': True,
            'role_fiscalizacao': True,
            'role_compat': True,
            'role_drenagem': True,
            'role_geoinfra': True,
            'role_selimp': True,
            'role_usuarios': True,
            'role_tickets': True,
            'role_cadastro_obra': True,
            'token': 'valid_access_token-in_group-gabriel.godoybz@hotmail.com'
        })

        response = controller(data)

        assert response.status_code == 200
        assert response.body["user"]["email"] == repo.users_list[0].email
        assert response.body["user"]["name"] == 'User Teste'
        assert response.body["user"]["enabled"] == False
        assert response.body["user"]["department"] == 'INTELICITY'
        assert response.body["user"]["role_dashboards"] == True
        assert response.body["user"]["role_fiscalizacao"] == True
        assert response.body["user"]["role_compat"] == True
        assert response.body["user"]["role_drenagem"] == True
        assert response.body["user"]["role_geoinfra"] == True
        assert response.body["user"]["role_selimp"] == True
        assert response.body["user"]["role_usuarios"] == True
        assert response.body["user"]["role_tickets"] == True
        assert response.body["user"]["role_cadastro_obra"] == True
        assert response.body["message"] == 'Usuário atualizado com sucesso!'
    
    def test_update_user_controller_missing_email(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboards': True,
            'role_fiscalizacao': True,
            'role_compat': True,
            'role_drenagem': True,
            'role_geoinfra': True,
            'role_selimp': True,
            'role_usuarios': True,
            'role_tickets': True,
            'role_cadastro_obra': True,
            'token': 'valid_access_token-in_group-gabriel.godoybz@hotmail.com'
        })

        response = controller(data)
        
        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: email'
    
    def test_update_user_controller_missing_user_id(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'email': repo.users_list[0].email,
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboards': True,
            'role_fiscalizacao': True,
            'role_compat': True,
            'role_drenagem': True,
            'role_geoinfra': True,
            'role_selimp': True,
            'role_usuarios': True,
            'role_tickets': True,
            'role_cadastro_obra': True,
        })

        response = controller(data)
        
        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: user_id'

    def test_update_user_controller_missing_name(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': repo.users_list[0].email,
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboards': True,
            'role_fiscalizacao': True,
            'role_compat': True,
            'role_drenagem': True,
            'role_geoinfra': True,
            'role_selimp': True,
            'role_usuarios': True,
            'role_tickets': True,
            'role_cadastro_obra': True,
            'token': 'valid_access_token-in_group-gabriel.godoybz@hotmail.com'
        })

        response = controller(data)
        
        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: name'
    
    def test_update_user_controller_missing_department(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': repo.users_list[0].email,
            'name': 'User Teste',
            'enabled': False,
            'role_dashboards': True,
            'role_fiscalizacao': True,
            'role_compat': True,
            'role_drenagem': True,
            'role_geoinfra': True,
            'role_selimp': True,
            'role_usuarios': True,
            'role_tickets': True,
            'role_cadastro_obra': True,
            'token': 'valid_access_token-in_group-gabriel.godoybz@hotmail.com'
        })

        response = controller(data)
        
        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: department'
    
    def test_update_user_controller_missing_enabled(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': repo.users_list[0].email,
            'name': 'User Teste',
            'department': 'INTELICITY',
            'role_dashboards': True,
            'role_fiscalizacao': True,
            'role_compat': True,
            'role_drenagem': True,
            'role_geoinfra': True,
            'role_selimp': True,
            'role_usuarios': True,
            'role_tickets': True,
            'role_cadastro_obra': True,
            'token': 'valid_access_token-in_group-gabriel.godoybz@hotmail.com'
        })

        response = controller(data)
        
        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: enabled'

    def test_update_user_controller_missing_role_dashboards(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': repo.users_list[0].email,
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_fiscalizacao': True,
            'role_compat': True,
            'role_drenagem': True,
            'role_geoinfra': True,
            'role_selimp': True,
            'role_usuarios': True,
            'role_tickets': True,
            'role_cadastro_obra': True,
            'token': 'valid_access_token-in_group-gabriel.godoybz@hotmail.com'
        })

        response = controller(data)
        
        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: role_dashboards'

    def test_update_user_controller_missing_role_fiscalizacao(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': repo.users_list[0].email,
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboards': True,
            'role_compat': True,
            'role_drenagem': True,
            'role_geoinfra': True,
            'role_selimp': True,
            'role_usuarios': True,
            'role_tickets': True,
            'role_cadastro_obra': True,
            'token': 'valid_access_token-in_group-gabriel.godoybz@hotmail.com'
        })

        response = controller(data)
        
        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: role_fiscalizacao'

    def test_update_user_controller_missing_role_compat(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': repo.users_list[0].email,
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboards': True,
            'role_fiscalizacao': True,
            'role_drenagem': True,
            'role_geoinfra': True,
            'role_selimp': True,
            'role_usuarios': True,
            'role_tickets': True,
            'role_cadastro_obra': True,
            'token': 'valid_access_token-in_group-gabriel.godoybz@hotmail.com'
        })

        response = controller(data)
        
        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: role_compat'

    def test_update_user_controller_missing_role_drenagem(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': repo.users_list[0].email,
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboards': True,
            'role_fiscalizacao': True,
            'role_compat': True,
            'role_geoinfra': True,
            'role_selimp': True,
            'role_usuarios': True,
            'role_tickets': True,
            'role_cadastro_obra': True,
            'token': 'valid_access_token-in_group-gabriel.godoybz@hotmail.com'
        })

        response = controller(data)
        
        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: role_drenagem'

    def test_update_user_controller_missing_role_geoinfra(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': repo.users_list[0].email,
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboards': True,
            'role_fiscalizacao': True,
            'role_compat': True,
            'role_drenagem': True,
            'role_selimp': True,
            'role_usuarios': True,
            'role_tickets': True,
            'role_cadastro_obra': True,
            'token': 'valid_access_token-in_group-gabriel.godoybz@hotmail.com'
        })

        response = controller(data)
        
        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: role_geoinfra'

    def test_update_user_controller_missing_role_selimp(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': repo.users_list[0].email,
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboards': True,
            'role_fiscalizacao': True,
            'role_compat': True,
            'role_drenagem': True,
            'role_geoinfra': True,
            'role_usuarios': True,
            'role_tickets': True,
            'role_cadastro_obra': True,
            'token': 'valid_access_token-in_group-gabriel.godoybz@hotmail.com'
        })

        response = controller(data)
        
        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: role_selimp'

    def test_update_user_controller_missing_role_usuarios(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': repo.users_list[0].email,
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboards': True,
            'role_fiscalizacao': True,
            'role_compat': True,
            'role_drenagem': True,
            'role_geoinfra': True,
            'role_selimp': True,
            'role_tickets': True,
            'role_cadastro_obra': True,
            'token': 'valid_access_token-in_group-gabriel.godoybz@hotmail.com'
        })

        response = controller(data)
        
        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: role_usuarios'

    def test_update_user_controller_missing_role_tickets(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': repo.users_list[0].email,
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboards': True,
            'role_fiscalizacao': True,
            'role_compat': True,
            'role_drenagem': True,
            'role_geoinfra': True,
            'role_selimp': True,
            'role_usuarios': True,
            'role_cadastro_obra': True,
            'token': 'valid_access_token-in_group-gabriel.godoybz@hotmail.com'
        })

        response = controller(data)
        
        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: role_tickets'

    def test_update_user_controller_missing_role_cadastro_obra(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': repo.users_list[0].email,
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboards': True,
            'role_fiscalizacao': True,
            'role_compat': True,
            'role_drenagem': True,
            'role_geoinfra': True,
            'role_selimp': True,
            'role_usuarios': True,
            'role_tickets': True,
            'token': 'valid_access_token-in_group-gabriel.godoybz@hotmail.com'
        })

        response = controller(data)
        
        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: role_cadastro_obra'