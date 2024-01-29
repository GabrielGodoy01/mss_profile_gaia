import datetime
from src.shared.domain.entities.user import User
from src.shared.infra.dtos.user_dynamo_dto import UserDynamoDTO
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_UserCognitoDTO:

    def test_from_entity(self):
        repo = UserRepositoryMock()
        user = User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45e124", email="joao@hotmail.com", name='João', department='Teste', role_cadastro_obra=True, role_compat=True, role_dashboards=True, role_drenagem=True, role_fiscalizacao=True, role_geoinfra=True, role_selimp=True, role_usuarios=True, role_tickets=True, enabled=True)

        user_cognito_dto = UserDynamoDTO.from_entity(user)

        user_cognito_dto_expected = UserDynamoDTO(
            email=user.email,
            name=user.name,
        )

        assert user_cognito_dto.email == user_cognito_dto_expected.email
        assert user_cognito_dto.name == user_cognito_dto_expected.name

    def test_from_entity_none(self):
        user = User(user_id="e73626b5-462d-4a3f-bef5-ae7cbb45e124", email="joao@hotmail.com", name='João', enabled=False)
        user_cognito_dto = UserDynamoDTO.from_entity(user)

        user_cognito_dto_expected = UserDynamoDTO(
            email=user.email,
            name=user.name,
        )
        
        assert user_cognito_dto.email == user_cognito_dto_expected.email
        assert user_cognito_dto.name == user_cognito_dto_expected.name

    def test_from_cognito(self):
        data = cognito_data = {'enabled': 'true',
                        'ResponseMetadata': {'HTTPHeaders': {'connection': 'keep-alive',
                                                             'content-length': '709',
                                                             'content-type': 'application/x-amz-json-1.1',
                                                             'date': 'Sat, 04 Feb 2023 13:45:05 GMT',
                                                             'x-amzn-requestid': '8b8fba2d-b2c7-4346-a441-e285892af0a3'},
                                             'HTTPStatusCode': 200,
                                             'RequestId': '8b8fba2d-b2c7-4346-a441-e285892af0a3',
                                             'RetryAttempts': 0},
                        'UserAttributes': [{'Name': 'custom:sector', 'Value': 'Teste'},
                                           {'Name': 'name', 'Value': 'joao'},
                                           {'Name': 'email', 'Value': 'joao@hotmail.com'},

                                           ],
                        'UserCreateDate': datetime.datetime(2023, 2, 3, 23, 27, 48, 713000),
                        'UserLastModifiedDate': datetime.datetime(2023, 2, 3, 23, 27, 48, 713000),
                        'UserStatus': 'UNCONFIRMED',
                        'Enabled': 'true',
                        'Username': 'vgsoller1@gmail.com'}

        user_cognito_dto = UserDynamoDTO.from_cognito(data)

        expected_dto = UserDynamoDTO(
            email="joao@hotmail.com",
            name="joao",
        )

        assert user_cognito_dto.email == expected_dto.email
        assert user_cognito_dto.name == expected_dto.name


    def test_to_dict(self):
        repo = UserRepositoryMock()

        user_cognito_dto = UserDynamoDTO(
            email = repo.users_list[0].email,
            name = repo.users_list[0].name,
        )

        user = user_cognito_dto.to_dict()

        assert user['email'] == repo.users_list[0].email
        assert user['name'] == repo.users_list[0].name