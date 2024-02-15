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
        assert user.role_dashboard_qualidade == True
        assert user.role_dashboard_deteccao == True
        assert user.role_dashboard_tempo == True
        assert user.role_dashboard_geoinfra == True
        assert user.role_dashboard_recapeamento == True
        assert user.role_dashboard_anel_viario == True
        assert user.role_dashboard_sist_unificado == True
        assert user.role_modfisc_convias == True
        assert user.role_modfisc_osmv == True
        assert user.role_modfisc_osct == True
        assert user.role_modfisc_relatoriomv == True
        assert user.role_modfisc_vistoriapv == True
        assert user.role_modfisc_vistoriarecape == True
        assert user.role_interf_mapa == True
        assert user.role_interf_protproc == True
        assert user.role_drenagem_ativos == True
        assert user.role_drenagem_redes == True
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
        assert user.role_dashboard_qualidade == None
        assert user.role_dashboard_deteccao == None
        assert user.role_dashboard_tempo == None
        assert user.role_dashboard_geoinfra == None
        assert user.role_dashboard_recapeamento == None
        assert user.role_dashboard_anel_viario == None
        assert user.role_dashboard_sist_unificado == None
        assert user.role_modfisc_convias == None
        assert user.role_modfisc_osmv == None
        assert user.role_modfisc_osct == None
        assert user.role_modfisc_relatoriomv == None
        assert user.role_modfisc_vistoriapv == None
        assert user.role_modfisc_vistoriarecape == None
        assert user.role_interf_mapa == None
        assert user.role_interf_protproc == None
        assert user.role_drenagem_ativos == None
        assert user.role_drenagem_redes == None
        assert user.role_usuarios == None
        assert user.role_tickets == None
