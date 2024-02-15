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
            'role_dashboard_qualidade': True,
            'role_dashboard_deteccao': True,
            'role_dashboard_tempo': True,
            'role_dashboard_geoinfra': True,
            'role_dashboard_recapeamento': True,
            'role_dashboard_anel_viario': True,
            'role_dashboard_sist_unificado': True,
            'role_modfisc_convias': True,
            'role_modfisc_osmv': True,
            'role_modfisc_osct': True,
            'role_modfisc_relatoriomv': True,
            'role_modfisc_vistoriapv': True,
            'role_modfisc_vistoriarecape': True,
            'role_interf_mapa': True,
            'role_interf_protproc': True,
            'role_drenagem_ativos': True,
            'role_drenagem_redes': True,
            'role_usuarios': True,
            'role_tickets': True,
            
        })

        response = controller(data)

        assert response.status_code == 200
        assert response.body["user"]["email"] == repo.users_list[0].email
        assert response.body["user"]["name"] == 'User Teste'
        assert response.body["user"]["enabled"] == False
        assert response.body["user"]["department"] == 'INTELICITY'
        assert response.body["user"]["role_dashboard_qualidade"] == True
        assert response.body["user"]["role_dashboard_deteccao"] == True
        assert response.body["user"]["role_dashboard_tempo"] == True
        assert response.body["user"]["role_dashboard_geoinfra"] == True
        assert response.body["user"]["role_dashboard_recapeamento"] == True
        assert response.body["user"]["role_dashboard_anel_viario"] == True
        assert response.body["user"]["role_dashboard_sist_unificado"] == True
        assert response.body["user"]["role_modfisc_convias"] == True
        assert response.body["user"]["role_modfisc_osmv"] == True
        assert response.body["user"]["role_modfisc_osct"] == True
        assert response.body["user"]["role_modfisc_relatoriomv"] == True
        assert response.body["user"]["role_modfisc_vistoriapv"] == True
        assert response.body["user"]["role_modfisc_vistoriarecape"] == True
        assert response.body["user"]["role_interf_mapa"] == True
        assert response.body["user"]["role_interf_protproc"] == True
        assert response.body["user"]["role_drenagem_ativos"] == True
        assert response.body["user"]["role_drenagem_redes"] == True
        assert response.body["user"]["role_usuarios"] == True
        assert response.body["user"]["role_tickets"] == True
    
    def test_update_user_controller_missing_email(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboard_qualidade': True,
            'role_dashboard_deteccao': True,
            'role_dashboard_tempo': True,
            'role_dashboard_geoinfra': True,
            'role_dashboard_recapeamento': True,
            'role_dashboard_anel_viario': True,
            'role_dashboard_sist_unificado': True,
            'role_modfisc_convias': True,
            'role_modfisc_osmv': True,
            'role_modfisc_osct': True,
            'role_modfisc_relatoriomv': True,
            'role_modfisc_vistoriapv': True,
            'role_modfisc_vistoriarecape': True,
            'role_interf_mapa': True,
            'role_interf_protproc': True,
            'role_drenagem_ativos': True,
            'role_drenagem_redes': True,
            'role_usuarios': True,
            'role_tickets': True,
            
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
            'role_dashboard_qualidade': True,
            'role_dashboard_deteccao': True,
            'role_dashboard_tempo': True,
            'role_dashboard_geoinfra': True,
            'role_dashboard_recapeamento': True,
            'role_dashboard_anel_viario': True,
            'role_dashboard_sist_unificado': True,
            'role_modfisc_convias': True,
            'role_modfisc_osmv': True,
            'role_modfisc_osct': True,
            'role_modfisc_relatoriomv': True,
            'role_modfisc_vistoriapv': True,
            'role_modfisc_vistoriarecape': True,
            'role_interf_mapa': True,
            'role_interf_protproc': True,
            'role_drenagem_ativos': True,
            'role_drenagem_redes': True,
            'role_usuarios': True,
            'role_tickets': True,
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
            'role_dashboard_qualidade': True,
            'role_dashboard_deteccao': True,
            'role_dashboard_tempo': True,
            'role_dashboard_geoinfra': True,
            'role_dashboard_recapeamento': True,
            'role_dashboard_anel_viario': True,
            'role_dashboard_sist_unificado': True,
            'role_modfisc_convias': True,
            'role_modfisc_osmv': True,
            'role_modfisc_osct': True,
            'role_modfisc_relatoriomv': True,
            'role_modfisc_vistoriapv': True,
            'role_modfisc_vistoriarecape': True,
            'role_interf_mapa': True,
            'role_interf_protproc': True,
            'role_drenagem_ativos': True,
            'role_drenagem_redes': True,
            'role_usuarios': True,
            'role_tickets': True,
            
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
            'role_dashboard_qualidade': True,
            'role_dashboard_deteccao': True,
            'role_dashboard_tempo': True,
            'role_dashboard_geoinfra': True,
            'role_dashboard_recapeamento': True,
            'role_dashboard_anel_viario': True,
            'role_dashboard_sist_unificado': True,
            'role_modfisc_convias': True,
            'role_modfisc_osmv': True,
            'role_modfisc_osct': True,
            'role_modfisc_relatoriomv': True,
            'role_modfisc_vistoriapv': True,
            'role_modfisc_vistoriarecape': True,
            'role_interf_mapa': True,
            'role_interf_protproc': True,
            'role_drenagem_ativos': True,
            'role_drenagem_redes': True,
            'role_usuarios': True,
            'role_tickets': True,
            
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
            'role_dashboard_qualidade': True,
            'role_dashboard_deteccao': True,
            'role_dashboard_tempo': True,
            'role_dashboard_geoinfra': True,
            'role_dashboard_recapeamento': True,
            'role_dashboard_anel_viario': True,
            'role_dashboard_sist_unificado': True,
            'role_modfisc_convias': True,
            'role_modfisc_osmv': True,
            'role_modfisc_osct': True,
            'role_modfisc_relatoriomv': True,
            'role_modfisc_vistoriapv': True,
            'role_modfisc_vistoriarecape': True,
            'role_interf_mapa': True,
            'role_interf_protproc': True,
            'role_drenagem_ativos': True,
            'role_drenagem_redes': True,
            'role_usuarios': True,
            'role_tickets': True,
            
        })

        response = controller(data)
        
        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: enabled'

    def test_update_user_controller_missing_role_dashboards_qualidade(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': repo.users_list[0].email,
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboard_deteccao': True,
            'role_dashboard_tempo': True,
            'role_dashboard_geoinfra': True,
            'role_dashboard_recapeamento': True,
            'role_dashboard_anel_viario': True,
            'role_dashboard_sist_unificado': True,
            'role_modfisc_convias': True,
            'role_modfisc_osmv': True,
            'role_modfisc_osct': True,
            'role_modfisc_relatoriomv': True,
            'role_modfisc_vistoriapv': True,
            'role_modfisc_vistoriarecape': True,
            'role_interf_mapa': True,
            'role_interf_protproc': True,
            'role_drenagem_ativos': True,
            'role_drenagem_redes': True,
            'role_usuarios': True,
            'role_tickets': True,
            
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: role_dashboard_qualidade'
    
    def test_update_user_controller_missing_role_dashboards_deteccao(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': repo.users_list[0].email,
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboard_qualidade': True,
            'role_dashboard_tempo': True,
            'role_dashboard_geoinfra': True,
            'role_dashboard_recapeamento': True,
            'role_dashboard_anel_viario': True,
            'role_dashboard_sist_unificado': True,
            'role_modfisc_convias': True,
            'role_modfisc_osmv': True,
            'role_modfisc_osct': True,
            'role_modfisc_relatoriomv': True,
            'role_modfisc_vistoriapv': True,
            'role_modfisc_vistoriarecape': True,
            'role_interf_mapa': True,
            'role_interf_protproc': True,
            'role_drenagem_ativos': True,
            'role_drenagem_redes': True,
            'role_usuarios': True,
            'role_tickets': True,
            
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: role_dashboard_deteccao'
    
    def test_update_user_controller_missing_role_dashboards_tempo(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': repo.users_list[0].email,
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboard_qualidade': True,
            'role_dashboard_deteccao': True,
            'role_dashboard_geoinfra': True,
            'role_dashboard_recapeamento': True,
            'role_dashboard_anel_viario': True,
            'role_dashboard_sist_unificado': True,
            'role_modfisc_convias': True,
            'role_modfisc_osmv': True,
            'role_modfisc_osct': True,
            'role_modfisc_relatoriomv': True,
            'role_modfisc_vistoriapv': True,
            'role_modfisc_vistoriarecape': True,
            'role_interf_mapa': True,
            'role_interf_protproc': True,
            'role_drenagem_ativos': True,
            'role_drenagem_redes': True,
            'role_usuarios': True,
            'role_tickets': True,
            
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: role_dashboard_tempo'
    
    def test_update_user_controller_missing_role_dashboards_geoinfra(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': repo.users_list[0].email,
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboard_qualidade': True,
            'role_dashboard_deteccao': True,
            'role_dashboard_tempo': True,
            'role_dashboard_recapeamento': True,
            'role_dashboard_anel_viario': True,
            'role_dashboard_sist_unificado': True,
            'role_modfisc_convias': True,
            'role_modfisc_osmv': True,
            'role_modfisc_osct': True,
            'role_modfisc_relatoriomv': True,
            'role_modfisc_vistoriapv': True,
            'role_modfisc_vistoriarecape': True,
            'role_interf_mapa': True,
            'role_interf_protproc': True,
            'role_drenagem_ativos': True,
            'role_drenagem_redes': True,
            'role_usuarios': True,
            'role_tickets': True,
            
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: role_dashboard_geoinfra'
    
    def test_update_user_controller_missing_role_dashboards_recapeamento(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': repo.users_list[0].email,
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboard_qualidade': True,
            'role_dashboard_deteccao': True,
            'role_dashboard_tempo': True,
            'role_dashboard_geoinfra': True,
            'role_dashboard_anel_viario': True,
            'role_dashboard_sist_unificado': True,
            'role_modfisc_convias': True,
            'role_modfisc_osmv': True,
            'role_modfisc_osct': True,
            'role_modfisc_relatoriomv': True,
            'role_modfisc_vistoriapv': True,
            'role_modfisc_vistoriarecape': True,
            'role_interf_mapa': True,
            'role_interf_protproc': True,
            'role_drenagem_ativos': True,
            'role_drenagem_redes': True,
            'role_usuarios': True,
            'role_tickets': True,
            
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: role_dashboard_recapeamento'
    
    def test_update_user_controller_missing_role_dashboards_anel_viario(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': repo.users_list[0].email,
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboard_qualidade': True,
            'role_dashboard_deteccao': True,
            'role_dashboard_tempo': True,
            'role_dashboard_geoinfra': True,
            'role_dashboard_recapeamento': True,
            'role_dashboard_sist_unificado': True,
            'role_modfisc_convias': True,
            'role_modfisc_osmv': True,
            'role_modfisc_osct': True,
            'role_modfisc_relatoriomv': True,
            'role_modfisc_vistoriapv': True,
            'role_modfisc_vistoriarecape': True,
            'role_interf_mapa': True,
            'role_interf_protproc': True,
            'role_drenagem_ativos': True,
            'role_drenagem_redes': True,
            'role_usuarios': True,
            'role_tickets': True,
            
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: role_dashboard_anel_viario'
    
    def test_update_user_controller_missing_role_dashboards_sist_unificado(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': repo.users_list[0].email,
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboard_qualidade': True,
            'role_dashboard_deteccao': True,
            'role_dashboard_tempo': True,
            'role_dashboard_geoinfra': True,
            'role_dashboard_recapeamento': True,
            'role_dashboard_anel_viario': True,
            'role_modfisc_convias': True,
            'role_modfisc_osmv': True,
            'role_modfisc_osct': True,
            'role_modfisc_relatoriomv': True,
            'role_modfisc_vistoriapv': True,
            'role_modfisc_vistoriarecape': True,
            'role_interf_mapa': True,
            'role_interf_protproc': True,
            'role_drenagem_ativos': True,
            'role_drenagem_redes': True,
            'role_usuarios': True,
            'role_tickets': True,
            
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: role_dashboard_sist_unificado'

    def test_update_user_controller_missing_role_modfisc_convias(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': repo.users_list[0].email,
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboard_qualidade': True,
            'role_dashboard_deteccao': True,
            'role_dashboard_tempo': True,
            'role_dashboard_geoinfra': True,
            'role_dashboard_recapeamento': True,
            'role_dashboard_anel_viario': True,
            'role_dashboard_sist_unificado': True,
            'role_modfisc_osmv': True,
            'role_modfisc_osct': True,
            'role_modfisc_relatoriomv': True,
            'role_modfisc_vistoriapv': True,
            'role_modfisc_vistoriarecape': True,
            'role_interf_mapa': True,
            'role_interf_protproc': True,
            'role_drenagem_ativos': True,
            'role_drenagem_redes': True,
            'role_usuarios': True,
            'role_tickets': True,
            
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: role_modfisc_convias'

    def test_update_user_controller_missing_role_modfisc_osmv(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': repo.users_list[0].email,
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboard_qualidade': True,
            'role_dashboard_deteccao': True,
            'role_dashboard_tempo': True,
            'role_dashboard_geoinfra': True,
            'role_dashboard_recapeamento': True,
            'role_dashboard_anel_viario': True,
            'role_dashboard_sist_unificado': True,
            'role_modfisc_convias': True,
            'role_modfisc_osct': True,
            'role_modfisc_relatoriomv': True,
            'role_modfisc_vistoriapv': True,
            'role_modfisc_vistoriarecape': True,
            'role_interf_mapa': True,
            'role_interf_protproc': True,
            'role_drenagem_ativos': True,
            'role_drenagem_redes': True,
            'role_usuarios': True,
            'role_tickets': True,
            
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: role_modfisc_osmv'
    
    def test_update_user_controller_missing_role_modfisc_osct(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': repo.users_list[0].email,
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboard_qualidade': True,
            'role_dashboard_deteccao': True,
            'role_dashboard_tempo': True,
            'role_dashboard_geoinfra': True,
            'role_dashboard_recapeamento': True,
            'role_dashboard_anel_viario': True,
            'role_dashboard_sist_unificado': True,
            'role_modfisc_convias': True,
            'role_modfisc_osmv': True,
            'role_modfisc_relatoriomv': True,
            'role_modfisc_vistoriapv': True,
            'role_modfisc_vistoriarecape': True,
            'role_interf_mapa': True,
            'role_interf_protproc': True,
            'role_drenagem_ativos': True,
            'role_drenagem_redes': True,
            'role_usuarios': True,
            'role_tickets': True,
            
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: role_modfisc_osct'
    
    def test_update_user_controller_missing_role_modfisc_relatoriomv(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': repo.users_list[0].email,
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboard_qualidade': True,
            'role_dashboard_deteccao': True,
            'role_dashboard_tempo': True,
            'role_dashboard_geoinfra': True,
            'role_dashboard_recapeamento': True,
            'role_dashboard_anel_viario': True,
            'role_dashboard_sist_unificado': True,
            'role_modfisc_convias': True,
            'role_modfisc_osmv': True,
            'role_modfisc_osct': True,
            'role_modfisc_vistoriapv': True,
            'role_modfisc_vistoriarecape': True,
            'role_interf_mapa': True,
            'role_interf_protproc': True,
            'role_drenagem_ativos': True,
            'role_drenagem_redes': True,
            'role_usuarios': True,
            'role_tickets': True,
            
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: role_modfisc_relatoriomv'


    def test_update_user_controller_missing_role_modfisc_vistoriapv(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': repo.users_list[0].email,
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboard_qualidade': True,
            'role_dashboard_deteccao': True,
            'role_dashboard_tempo': True,
            'role_dashboard_geoinfra': True,
            'role_dashboard_recapeamento': True,
            'role_dashboard_anel_viario': True,
            'role_dashboard_sist_unificado': True,
            'role_modfisc_convias': True,
            'role_modfisc_osmv': True,
            'role_modfisc_osct': True,
            'role_modfisc_relatoriomv': True,
            'role_modfisc_vistoriarecape': True,
            'role_interf_mapa': True,
            'role_interf_protproc': True,
            'role_drenagem_ativos': True,
            'role_drenagem_redes': True,
            'role_usuarios': True,
            'role_tickets': True,
            
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: role_modfisc_vistoriapv'

    def test_update_user_controller_missing_role_modfisc_vistoriarecape(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': repo.users_list[0].email,
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboard_qualidade': True,
            'role_dashboard_deteccao': True,
            'role_dashboard_tempo': True,
            'role_dashboard_geoinfra': True,
            'role_dashboard_recapeamento': True,
            'role_dashboard_anel_viario': True,
            'role_dashboard_sist_unificado': True,
            'role_modfisc_convias': True,
            'role_modfisc_osmv': True,
            'role_modfisc_osct': True,
            'role_modfisc_relatoriomv': True,
            'role_modfisc_vistoriapv': True,
            'role_interf_mapa': True,
            'role_interf_protproc': True,
            'role_drenagem_ativos': True,
            'role_drenagem_redes': True,
            'role_usuarios': True,
            'role_tickets': True,
            
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: role_modfisc_vistoriarecape'
    
    def test_update_user_controller_missing_role_interf_mapa(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': repo.users_list[0].email,
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboard_qualidade': True,
            'role_dashboard_deteccao': True,
            'role_dashboard_tempo': True,
            'role_dashboard_geoinfra': True,
            'role_dashboard_recapeamento': True,
            'role_dashboard_anel_viario': True,
            'role_dashboard_sist_unificado': True,
            'role_modfisc_convias': True,
            'role_modfisc_osmv': True,
            'role_modfisc_osct': True,
            'role_modfisc_relatoriomv': True,
            'role_modfisc_vistoriapv': True,
            'role_modfisc_vistoriarecape': True,
            'role_interf_protproc': True,
            'role_drenagem_ativos': True,
            'role_drenagem_redes': True,
            'role_usuarios': True,
            'role_tickets': True,
            
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: role_interf_mapa'

    def test_update_user_controller_missing_role_interf_protproc(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': repo.users_list[0].email,
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboard_qualidade': True,
            'role_dashboard_deteccao': True,
            'role_dashboard_tempo': True,
            'role_dashboard_geoinfra': True,
            'role_dashboard_recapeamento': True,
            'role_dashboard_anel_viario': True,
            'role_dashboard_sist_unificado': True,
            'role_modfisc_convias': True,
            'role_modfisc_osmv': True,
            'role_modfisc_osct': True,
            'role_modfisc_relatoriomv': True,
            'role_modfisc_vistoriapv': True,
            'role_modfisc_vistoriarecape': True,
            'role_interf_mapa': True,
            'role_drenagem_ativos': True,
            'role_drenagem_redes': True,
            'role_usuarios': True,
            'role_tickets': True,
            
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: role_interf_protproc'
    
    def test_update_user_controller_missing_role_drenagem_ativos(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': repo.users_list[0].email,
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboard_qualidade': True,
            'role_dashboard_deteccao': True,
            'role_dashboard_tempo': True,
            'role_dashboard_geoinfra': True,
            'role_dashboard_recapeamento': True,
            'role_dashboard_anel_viario': True,
            'role_dashboard_sist_unificado': True,
            'role_modfisc_convias': True,
            'role_modfisc_osmv': True,
            'role_modfisc_osct': True,
            'role_modfisc_relatoriomv': True,
            'role_modfisc_vistoriapv': True,
            'role_modfisc_vistoriarecape': True,
            'role_interf_mapa': True,
            'role_interf_protproc': True,
            'role_drenagem_redes': True,
            'role_usuarios': True,
            'role_tickets': True,
            
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: role_drenagem_ativos'
    
    def test_update_user_controller_missing_role_drenagem_redes(self):
        repo = UserRepositoryMock()
        usecase = UpdateUserUsecase(repo)

        controller = UpdateUserController(usecase)

        data = HttpRequest(body={
            'user_id': "e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            'email': repo.users_list[0].email,
            'name': 'User Teste',
            'enabled': False,
            'department': 'INTELICITY',
            'role_dashboard_qualidade': True,
            'role_dashboard_deteccao': True,
            'role_dashboard_tempo': True,
            'role_dashboard_geoinfra': True,
            'role_dashboard_recapeamento': True,
            'role_dashboard_anel_viario': True,
            'role_dashboard_sist_unificado': True,
            'role_modfisc_convias': True,
            'role_modfisc_osmv': True,
            'role_modfisc_osct': True,
            'role_modfisc_relatoriomv': True,
            'role_modfisc_vistoriapv': True,
            'role_modfisc_vistoriarecape': True,
            'role_interf_mapa': True,
            'role_interf_protproc': True,
            'role_drenagem_ativos': True,
            'role_usuarios': True,
            'role_tickets': True,
            
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: role_drenagem_redes'

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
            'role_dashboard_qualidade': True,
            'role_dashboard_deteccao': True,
            'role_dashboard_tempo': True,
            'role_dashboard_geoinfra': True,
            'role_dashboard_recapeamento': True,
            'role_dashboard_anel_viario': True,
            'role_dashboard_sist_unificado': True,
            'role_modfisc_convias': True,
            'role_modfisc_osmv': True,
            'role_modfisc_osct': True,
            'role_modfisc_relatoriomv': True,
            'role_modfisc_vistoriapv': True,
            'role_modfisc_vistoriarecape': True,
            'role_interf_mapa': True,
            'role_interf_protproc': True,
            'role_drenagem_ativos': True,
            'role_drenagem_redes': True,
            'role_tickets': True,
            
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
            'role_dashboard_qualidade': True,
            'role_dashboard_deteccao': True,
            'role_dashboard_tempo': True,
            'role_dashboard_geoinfra': True,
            'role_dashboard_recapeamento': True,
            'role_dashboard_anel_viario': True,
            'role_dashboard_sist_unificado': True,
            'role_modfisc_convias': True,
            'role_modfisc_osmv': True,
            'role_modfisc_osct': True,
            'role_modfisc_relatoriomv': True,
            'role_modfisc_vistoriapv': True,
            'role_modfisc_vistoriarecape': True,
            'role_interf_mapa': True,
            'role_interf_protproc': True,
            'role_drenagem_ativos': True,
            'role_drenagem_redes': True,
            'role_usuarios': True,
        })

        response = controller(data)

        assert response.status_code == 400
        assert response.body["message"] == 'Parâmetro ausente: role_tickets'