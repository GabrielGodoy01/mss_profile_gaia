import pytest
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.user_repository_db import UserRepositoryDynamo


class Test_UserRepositoryDb:
    
    @pytest.mark.skip("Can't test dynamo in Github")
    def test_check_user_group(self):
        repo = UserRepositoryDynamo()
        resp = repo.check_user_group(email="gabriel.godoybz@hotmail.com")
        assert resp == True

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_check_user_group_wrong_email(self):
        repo = UserRepositoryDynamo()
        with pytest.raises(NoItemsFound):
            repo.check_user_group(email="123")        
