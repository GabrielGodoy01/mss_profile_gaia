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

            if response['UserStatus'] == 'CONFIRMED':
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
        
        item = UserDynamoDTO.from_entity(user=user).to_dynamo()

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
                "role_dashboard_qualidade": new_user_data.role_dashboard_qualidade,
                "role_dashboard_deteccao": new_user_data.role_dashboard_deteccao,
                "role_dashboard_tempo": new_user_data.role_dashboard_tempo,
                "role_dashboard_geoinfra": new_user_data.role_dashboard_geoinfra,
                "role_dashboard_recapeamento": new_user_data.role_dashboard_recapeamento,
                "role_dashboard_anel_viario": new_user_data.role_dashboard_anel_viario,
                "role_dashboard_sist_unificado": new_user_data.role_dashboard_sist_unificado,
                "role_modfisc_convias": new_user_data.role_modfisc_convias,
                "role_modfisc_osmv": new_user_data.role_modfisc_osmv,
                "role_modfisc_osct": new_user_data.role_modfisc_osct,
                "role_modfisc_relatoriomv": new_user_data.role_modfisc_relatoriomv,
                "role_modfisc_vistoriapv": new_user_data.role_modfisc_vistoriapv,
                "role_modfisc_vistoriarecape": new_user_data.role_modfisc_vistoriarecape,
                "role_interf_mapa": new_user_data.role_interf_mapa,
                "role_interf_protproc": new_user_data.role_interf_protproc,
                "role_drenagem_ativos": new_user_data.role_drenagem_ativos,
                "role_drenagem_redes": new_user_data.role_drenagem_redes,
                "role_usuarios": new_user_data.role_usuarios,
                "role_tickets": new_user_data.role_tickets
            })

        if "Attributes" not in response:
            return None

        return UserDynamoDTO.from_dynamo(response["Attributes"]).to_entity()