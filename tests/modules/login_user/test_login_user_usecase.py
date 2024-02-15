import pytest
from src.modules.login_user.app.login_user_usecase import LoginUserUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import InvalidCredentials
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_LoginUserUsecase:

    def test_login_user_usecase(self):
        repo = UserRepositoryMock()
        usecase = LoginUserUsecase(repo)

        user = usecase(user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e123', name='Gabriel', email='gabriel@hotmail.com', groups=['INTELICITY'])

        assert user.user_id == 'e73626b5-462d-4a3f-bef5-ae7cbb45e123'
        assert user.email == 'gabriel@hotmail.com'
        assert user.name == 'Gabriel'
        assert user.department == 'INTELICITY'
        assert user.enabled == True
        assert user.role_cadastro_obra == True
        assert user.role_compat == True
        assert user.role_dashboards == True
        assert user.role_drenagem == True
        assert user.role_fiscalizacao == True
        assert user.role_geoinfra == True
        assert user.role_selimp == True
        assert user.role_usuarios == True
        assert user.role_tickets == True
    
    def test_login_user_usecase_invalid_token(self):
        repo = UserRepositoryMock()
        usecase = LoginUserUsecase(repo)

        with pytest.raises(EntityError):
            user = usecase(user_id='e73626b5-462d-4a3f-bef5-ae7', name='Gabriel', email='gabriel@hotmail.com', groups=['GAIA'])
    
    def test_login_user_usecase_not_in_group(self):
        repo = UserRepositoryMock()
        usecase = LoginUserUsecase(repo)

        with pytest.raises(InvalidCredentials):
            user = usecase(user_id='e73626b5-462d-4a3f-bef5-ae7', name='Gabriel', email='gabriel@hotmail.com', groups=[''])
    
    def test_login_user_usecase_create_new_user(self):
        repo = UserRepositoryMock()
        usecase = LoginUserUsecase(repo)
        user = usecase(user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e124', name='Gabriel', email='gabriel@hotmail.com', groups=['GAIA'])

        assert user.user_id == 'e73626b5-462d-4a3f-bef5-ae7cbb45e124'
        assert user.email == 'gabriel@hotmail.com'
        assert user.name == 'Gabriel'
        assert user.department == None
        assert user.enabled == True
        assert user.role_cadastro_obra == None
        assert user.role_compat == None
        assert user.role_dashboards == None
        assert user.role_drenagem == None
        assert user.role_fiscalizacao == None
        assert user.role_geoinfra == None
        assert user.role_selimp == None
        assert user.role_usuarios == None
        assert user.role_tickets == None
