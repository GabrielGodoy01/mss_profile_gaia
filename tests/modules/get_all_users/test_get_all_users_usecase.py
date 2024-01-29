import pytest
from src.modules.get_all_users.app.get_all_users_usecase import GetAllUsersUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetAllUsersUsecase:
    def test_get_all_users_usecase(self):
        repo = UserRepositoryMock()
        usecase = GetAllUsersUsecase(repo)

        all_users = usecase(user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e123')

        assert len(all_users) == 2
    
    def test_get_all_users_usecase_not_created(self):
        repo = UserRepositoryMock()
        usecase = GetAllUsersUsecase(repo)

        repo.users = []

        with pytest.raises(NoItemsFound):
            usecase(user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e124')
    
    def test_get_all_users_usecase_not_adm(self):
        repo = UserRepositoryMock()
        usecase = GetAllUsersUsecase(repo)

        with pytest.raises(ForbiddenAction):
            usecase(user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e456')
