import pytest
from src.shared.domain.entities.user import User
from src.shared.helpers.errors.domain_errors import EntityError

class Test_User:

    def test_user(self):
        User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email="gabriel.godoybz@hotmail.com", name='Gabriel', department='CONVIAS', role_cadastro_obra=True, role_compat=True, role_dashboards=True, role_drenagem=True, role_fiscalizacao=True, role_geoinfra=True, role_selimp=True, role_usuarios=True, role_tickets=True, enabled=True,)
    
    def test_user_id_is_none(self):
        with pytest.raises(EntityError):
            User(user_id=None,email='gabriel.godoybz@hotmail.com', name='Gabriel', department='Teste', enabled=True)
    
    def test_user_id_is_not_str(self):
        with pytest.raises(EntityError):
            User(user_id=123, email='gabriel.godoybz@hotmail.com', name='Gabriel', department='Teste', enabled=True)
    
    def test_user_id_is_not_validate(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5", email='gabriel.godoybz@hotmail.com', name='Gabriel', department='Teste', enabled=True)

    def test_user_email_is_none(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93",email=None, name='Gabriel', department='Teste', enabled=True)
    
    def test_user_email_is_not_str(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email=123, name='Gabriel', department='Teste', enabled=True)
    
    def test_user_email_is_not_validate(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel', name='Gabriel', department='Teste', enabled=True)
    
    def test_user_name_is_none(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel.godoybz@hotmail.com', name=None, department='Teste', enabled=True)
    
    def test_user_name_is_not_str(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel.godoybz@hotmail.com', name=123, department='Teste', enabled=True)
    
    def test_user_name_is_not_min_length(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel.godoybz@hotmail.com', name='GA', enabled=True)
    
    def test_user_department_is_not_str(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel.godoybz@hotmail.com', name='Gabriel', department=123, enabled=True)
    
    def test_user_role_dashboards_is_not_role_enum(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel.godoybz@hotmail.com', name='Gabriel', department='123', role_dashboards=123, enabled=True)
    
    def test_user_role_fiscalizacao_is_not_role_enum(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel.godoybz@hotmail.com', name='Gabriel', department='123', role_fiscalizacao=123, enabled=True)
    
    def test_user_role_geoinfra_is_not_role_enum(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel.godoybz@hotmail.com', name='Gabriel', department='123', role_geoinfra=123, enabled=True)
    
    def test_user_role_drenagem_is_not_role_enum(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel.godoybz@hotmail.com', name='Gabriel', department='123', role_drenagem=123, enabled=True)

    def test_user_role_usuarios_is_not_role_enum(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel.godoybz@hotmail.com', name='Gabriel', department='123', role_usuarios=123, enabled=True)

    def test_user_role_tickets_is_not_role_enum(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel.godoybz@hotmail.com', name='Gabriel', department='123', role_tickets=123, enabled=True)
    
    def test_user_role_cadastro_obra_is_not_role_enum(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel.godoybz@hotmail.com', name='Gabriel', department='123', role_cadastro_obra=123, enabled=True)

    def test_user_role_selimp_is_not_role_enum(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel.godoybz@hotmail.com', name='Gabriel', department='123', role_selimp=123, enabled=True)
    
    def test_user_role_compat_is_not_role_enum(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email='gabriel.godoybz@hotmail.com', name='Gabriel', department='123', role_compat=123, enabled=True)
    
    def test_user_enabled_is_none(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email="gabriel.godoybz@hotmail.com", name='Gabriel', department='Teste', role_cadastro_obra=True, role_compat=True, role_dashboards=True, role_drenagem=True, role_fiscalizacao=True, role_geoinfra=True, role_selimp=True, role_usuarios=True, role_tickets=True, enabled=None)
    
    def test_user_enabled_is_not_bool(self):
        with pytest.raises(EntityError):
            User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45ea93", email="gabriel.godoybz@hotmail.com", name='Gabriel', department='Teste', role_cadastro_obra=True, role_compat=True, role_dashboards=True, role_drenagem=True, role_fiscalizacao=True, role_geoinfra=True, role_selimp=True, role_usuarios=True, role_tickets=True, enabled=123)