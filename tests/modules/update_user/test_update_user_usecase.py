import pytest
from src.modules.update_user.app.update_user_usecase import UpdateUserUsecase
from src.shared.domain.entities.user import User
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_UpdateUserUsecase:
    def test_update_user_usecase(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        user = usecase(new_user_data=User(user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e123',email=repo.users_list[0].email, name='User Teste', enabled=False))

        assert user.email == 'gabriel.godoybz@hotmail.com'
        assert user.name == 'User Teste'
        assert user.enabled == False
    
    def test_update_user_usecase_not_created(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        with pytest.raises(NoItemsFound):
            usecase(new_user_data=User(user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e124', email=repo.users_list[0].email, name='User Teste', enabled=False))
    
    def test_update_user_usecase_not_adm(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        with pytest.raises(ForbiddenAction):
            usecase(new_user_data=User(user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e456', email=repo.users_list[0].email, name='User Teste', enabled=False))