from src.modules.login_user.app.login_user_controller import LoginUserController
from src.modules.login_user.app.login_user_usecase import LoginUserUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_LoginUserController:
    def test_login_user_controller(self):
        repo = UserRepositoryMock()
        usecase = LoginUserUsecase(repo)

        controller = LoginUserController(usecase)

        request = HttpRequest(body={
          'user_id': 'e73626b5-462d-4a3f-bef5-ae7cbb45e123',
          'name': 'Gabriel',
          'email': 'gabriel@hotmail.com',
          'groups': ['GAIA']
        })

        response = controller(request)

        assert response.status_code == 200
        assert response.body["user"]["email"] == repo.users_list[0].email
        assert response.body["user"]["name"] == repo.users_list[0].name
        assert response.body["user"]["role_cadastro_obra"] == repo.users_list[0].role_cadastro_obra
        assert response.body["user"]["role_compat"] == repo.users_list[0].role_compat
        assert response.body["user"]["role_dashboards"] == repo.users_list[0].role_dashboards
        assert response.body["user"]["role_drenagem"] == repo.users_list[0].role_drenagem
        assert response.body["user"]["role_fiscalizacao"] == repo.users_list[0].role_fiscalizacao
        assert response.body["user"]["role_geoinfra"] == repo.users_list[0].role_geoinfra
        assert response.body["user"]["role_selimp"] == repo.users_list[0].role_selimp
        assert response.body["user"]["role_usuarios"] == repo.users_list[0].role_usuarios
        assert response.body["user"]["role_tickets"] == repo.users_list[0].role_tickets
        assert response.body["message"] == "Login realizado com sucesso!"
    
    
    def test_login_user_controller_with_missing_user_id(self):
        repo = UserRepositoryMock()
        usecase = LoginUserUsecase(repo)

        controller = LoginUserController(usecase)

        request = HttpRequest(body={
          'name': 'Gabriel',
          'email': 'gabriel@hotmail.com',
          'groups': ['GAIA']
        })

        response = controller(request)
        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: user_id'
    
    def test_login_user_controller_with_missing_name(self):
        repo = UserRepositoryMock()
        usecase = LoginUserUsecase(repo)

        controller = LoginUserController(usecase)

        request = HttpRequest(body={
          'user_id': 'e73626b5-462d-4a3f-bef5-ae7cbb45e123',
          'email': 'gabriel@hotmail.com',
          'groups': ['GAIA']
        })

        response = controller(request)
        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: name'
    
    def test_login_user_controller_with_missing_email(self):
        repo = UserRepositoryMock()
        usecase = LoginUserUsecase(repo)

        controller = LoginUserController(usecase)

        request = HttpRequest(body={
          'user_id': 'e73626b5-462d-4a3f-bef5-ae7cbb45e123',
          'name': 'Gabriel',
          'groups': ['GAIA']
        })

        response = controller(request)
        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: email'
      
    def test_login_user_controller_with_missing_groups(self):
        repo = UserRepositoryMock()
        usecase = LoginUserUsecase(repo)

        controller = LoginUserController(usecase)

        request = HttpRequest(body={
          'user_id': 'e73626b5-462d-4a3f-bef5-ae7cbb45e123',
          'email': 'gabriel@hotmail.com',
          'name': 'Gabriel',
        })

        response = controller(request)
        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: groups'