from src.modules.get_all_users.app.get_all_users_controller import GetAllUsersController
from src.modules.get_all_users.app.get_all_users_usecase import GetAllUsersUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetAllUsersController:
    
    def test_get_all_users_controller(self):
        repo = UserRepositoryMock()
        usecase = GetAllUsersUsecase(repo)
        controller = GetAllUsersController(usecase)

        request = HttpRequest(body={
                'user_id': 'e73626b5-462d-4a3f-bef5-ae7cbb45e123',
            })

        response = controller(request)

        assert response.status_code == 200
        assert len(response.body['user_list']) == 2
        assert response.body['message'] == 'Usuários retornados com sucesso!'
    
    def test_get_all_users_controller_with_missing_user_id(self):
        repo = UserRepositoryMock()
        usecase = GetAllUsersUsecase(repo)
        controller = GetAllUsersController(usecase)

        response = controller(HttpRequest(body={}))

        assert response.status_code == 400
        assert response.body['message'] == 'Parâmetro ausente: user_id'