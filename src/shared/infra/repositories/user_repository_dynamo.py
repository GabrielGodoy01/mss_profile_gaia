from typing import List, Optional
import boto3
from src.shared.domain.entities.user import User
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.environments import Environments
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, InvalidTokenError, NoItemsFound, UserNotValid
from src.shared.infra.dtos.user_dynamo_dto import UserDynamoDTO
from botocore.exceptions import ClientError

from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource


class UserRepositoryDynamo(IUserRepository):
    def __init__(self):
        self.client_cognito = boto3.client('cognito-idp', region_name=Environments.get_envs().region)
        self.user_pool_id = Environments.get_envs().user_pool_id
        self.dynamo = DynamoDatasource(endpoint_url=Environments.get_envs().endpoint_url,
                                       dynamo_table_name=Environments.get_envs().dynamo_table_name,
                                       region=Environments.get_envs().region,
                                       partition_key=Environments.get_envs().dynamo_partition_key,
                                       )

    @staticmethod
    def partition_key_format(user_id: str) -> str:
        return f"{user_id}"
    
    def check_user_id_cognito(self, user_id: str) -> bool:
        try:
            response = self.client_cognito.admin_get_user(
                UserPoolId=self.user_pool_id,
                Username=user_id
            )

            if not response['UserStatus'] == 'CONFIRMED':
                return True

            return False
        except ClientError as e:
            error_code = e.response.get('Error').get('Code')
            if error_code == 'NotAuthorizedException':
                raise InvalidTokenError(message="Token inválido ou expirado")
            else:
                raise ForbiddenAction(message=e.response.get('Error').get('Message'))        
    
    def get_user_by_id(self, user_id: str) -> Optional[User]:
        user_data = self.dynamo.get_item(partition_key=self.partition_key_format(user_id=user_id))                    
        
        if 'Item' not in user_data:
            return None

        user = UserDynamoDTO.from_dynamo(user_data.get("Item")).to_entity()

        return user

    def get_all_users(self) -> List[User]:
        response = self.dynamo.get_all_items()

        users= list()

        for item in response["Items"]:
            users.append(UserDynamoDTO.from_dynamo(item).to_entity())
        
        return users

    def create_profile(self, user: User) -> User:
        if not self.check_user_id_cognito(user_id=user.user_id):
            raise UserNotValid(message="Usuário inválido")
        
        user_dto = UserDynamoDTO.from_entity(user=user)
        item = user_dto.to_dynamo()

        resp = self.dynamo.put_item(
            partition_key=self.partition_key_format(user.user_id),
            item=item,
            is_decimal=True
        )

        return user

    def update_user_by_id(self, new_user_data: User) -> User:
        user_to_update = self.get_user_by_id(user_id=new_user_data.user_id)

        if user_to_update is None: 
            return None

        response = self.dynamo.update_item(
            partition_key=self.partition_key_format(user_id=new_user_data.user_id),
            sort_key=None,
            update_dict={
                "name": new_user_data.name, 
                "email": new_user_data.email, 
                "enabled": new_user_data.enabled, 
                "department": new_user_data.department, 
                "role_dashboards": new_user_data.role_dashboards,
                "role_fiscalizacao": new_user_data.role_fiscalizacao,
                "role_geoinfra": new_user_data.role_geoinfra,
                "role_drenagem": new_user_data.role_drenagem,
                "role_usuarios": new_user_data.role_usuarios,
                "role_tickets": new_user_data.role_tickets,
                "role_cadastro_obra": new_user_data.role_cadastro_obra,
                "role_selimp": new_user_data.role_selimp,
                "role_compat": new_user_data.role_compat
            })

        if "Attributes" not in response:
            return None

        return UserDynamoDTO.from_dynamo(response["Attributes"]).to_entity()