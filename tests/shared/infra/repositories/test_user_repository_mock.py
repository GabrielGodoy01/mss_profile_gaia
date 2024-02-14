import pytest
from src.shared.domain.entities.user import User
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_UserRepositoryMock:
    
    def test_get_user_by_id(self):
        repo = UserRepositoryMock()
        user = repo.get_user_by_id(user_id='e73626b5-462d-4a3f-bef5-ae7cbb45e123')

        assert user.name == 'Gabriel'
        assert type(user) == User
    
    def test_get_all_users(self):
        repo = UserRepositoryMock()
        users = repo.get_all_users()

        assert type(users[0]) == User
        assert type(users) == list
        assert users[0].name == 'Gabriel'
        assert len(users) == 2
    
    def test_create_profile(self):
        repo = UserRepositoryMock()
        user_to_create = User(
            user_id="e73626b5-462d-4a3f-bef5-ae7cbb45e123",
            email="gabriel.godoybz@gmail.com",
            name="User Teste",
            enabled=True,
        )
        user = repo.create_profile(
                user=user_to_create
        )

        assert user.name == 'User Teste'
        assert user.enabled == True
    
    def test_update_user(self):
        repo = UserRepositoryMock()
        repo.update_user_by_id(
            new_user_data=User(
                user_id="e73626b5-462d-4a3f-bef5-ae7cbb45e123",
                email="gabriel.godoybz@hotmail.com",
                name="User Teste",
                enabled=False,
                role_cadastro_obra=False,
                role_compat=False,
                role_dashboards=False,
                role_drenagem=False,
                role_fiscalizacao=False,
                role_geoinfra=False,
                role_selimp=False,
                role_tickets=False,
                role_usuarios=False,
                department='Teste'
            )
        )

        assert repo.users_list[0].name == 'User Teste'
        assert repo.users_list[0].enabled == False
        assert repo.users_list[0].role_cadastro_obra == False
        assert repo.users_list[0].role_compat == False
        assert repo.users_list[0].role_dashboards == False
        assert repo.users_list[0].role_drenagem == False
        assert repo.users_list[0].role_fiscalizacao == False
        assert repo.users_list[0].role_geoinfra == False
        assert repo.users_list[0].role_selimp == False
        assert repo.users_list[0].role_tickets == False
        assert repo.users_list[0].role_usuarios == False
        assert repo.users_list[0].department == 'Teste'

    def test_update_user_non_exists(self):
        repo = UserRepositoryMock()
        user = repo.update_user_by_id(
            new_user_data=User(
                user_id="e73626b5-462d-4a3f-bef5-ae7cbb45e124",
                email="gabriel@godoybz.com",
                name="User Teste",
                enabled=False,
                role_cadastro_obra=False,
                role_compat=False,
                role_dashboards=False,
                role_drenagem=False,
                role_fiscalizacao=False,
                role_geoinfra=False,
                role_selimp=False,
                role_tickets=False,
                role_usuarios=False,
                department='Teste'
            )
        )
        assert user == None