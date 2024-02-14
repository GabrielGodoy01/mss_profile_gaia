from typing import Optional
from src.shared.domain.entities.user import User


class UserDynamoDTO:
    user_id: str
    email: str
    name: str
    enabled: bool
    department: Optional[str] = None
    role_dashboards: Optional[bool] = None
    role_fiscalizacao: Optional[bool] = None
    role_geoinfra: Optional[bool] = None
    role_drenagem: Optional[bool] = None
    role_usuarios: Optional[bool] = None
    role_tickets: Optional[bool] = None
    role_cadastro_obra: Optional[bool] = None
    role_selimp: Optional[bool] = None
    role_compat: Optional[bool] = None


    def __init__(self, user_id: str, email: str, name: str, enabled: bool, department: Optional[str] = None, role_dashboards: Optional[bool] = None, 
            role_fiscalizacao: Optional[bool] = None,
            role_geoinfra: Optional[bool] = None,
            role_drenagem: Optional[bool] = None,
            role_usuarios: Optional[bool] = None,
            role_tickets: Optional[bool] = None,
            role_cadastro_obra: Optional[bool] = None,
            role_selimp: Optional[bool] = None,
            role_compat: Optional[bool] = None,):
        self.email = email
        self.name = name
        self.user_id = user_id
        self.enabled = enabled
        self.department = department
        self.role_dashboards = role_dashboards
        self.role_fiscalizacao = role_fiscalizacao
        self.role_geoinfra = role_geoinfra
        self.role_drenagem = role_drenagem
        self.role_usuarios = role_usuarios
        self.role_tickets = role_tickets
        self.role_cadastro_obra = role_cadastro_obra
        self.role_selimp = role_selimp
        self.role_compat = role_compat

    @staticmethod
    def from_entity(user: User):
        return UserDynamoDTO(
            email=user.email,
            name=user.name,
            user_id=user.user_id,
            enabled=user.enabled,
            department=user.department,
            role_dashboards=user.role_dashboards,
            role_fiscalizacao=user.role_fiscalizacao,
            role_geoinfra=user.role_geoinfra,
            role_drenagem=user.role_drenagem,
            role_usuarios=user.role_usuarios,
            role_tickets=user.role_tickets,
            role_cadastro_obra=user.role_cadastro_obra,
            role_selimp=user.role_selimp,
            role_compat=user.role_compat
        )

    def to_dynamo(self) -> dict:
        """
        Parse data from UserDynamoDTO to dict
        """
        data = {
            "name": self.name,
            "email": self.email,
            "user_id": self.user_id,
            "enabled": self.enabled,
            "department": self.department if self.department is not None else None,
            "role_dashboards": self.role_dashboards if self.role_dashboards is not None else None,
            "role_fiscalizacao": self.role_fiscalizacao if self.role_fiscalizacao is not None else None,
            "role_geoinfra": self.role_geoinfra if self.role_geoinfra is not None else None,
            "role_drenagem": self.role_drenagem if self.role_drenagem is not None else None,
            "role_usuarios": self.role_usuarios if self.role_usuarios is not None else None,
            "role_tickets": self.role_tickets if self.role_tickets is not None else None,
            "role_cadastro_obra": self.role_cadastro_obra if self.role_cadastro_obra is not None else None,
            "role_selimp": self.role_selimp if self.role_selimp is not None else None,
            "role_compat": self.role_compat if self.role_compat is not None else None
        }

        data_without_none_values = {k: v for k, v in data.items() if v is not None}

        return data_without_none_values

    @staticmethod
    def from_dynamo(user_data: dict) -> "UserDynamoDTO":
        """
        Parse data from DynamoDB to UserDynamoDTO
        @param user_data: dict from DynamoDB
        """
        return UserDynamoDTO(
            name=str(user_data["name"]),
            email=str(user_data["email"]),
            user_id=str(user_data["user_id"]),
            enabled=bool(user_data["enabled"]),
            department=str(user_data["department"]),
            role_dashboards=bool(user_data["role_dashboards"]),
            role_fiscalizacao=bool(user_data["role_fiscalizacao"]),
            role_geoinfra=bool(user_data["role_geoinfra"]),
            role_drenagem=bool(user_data["role_drenagem"]),
            role_usuarios=bool(user_data["role_usuarios"]),
            role_tickets=bool(user_data["role_tickets"]),
            role_cadastro_obra=bool(user_data["role_cadastro_obra"]),
            role_selimp=bool(user_data["role_selimp"]),
            role_compat=bool(user_data["role_compat"]),
        )
    
    def to_entity(self) -> User:
        """
        Parse data from UserDynamoDTO to User
        """
        return User(
            name=self.name,
            email=self.email,
            user_id=self.user_id,
            enabled=self.enabled,
            department=self.department,
            role_dashboards=self.role_dashboards,
            role_fiscalizacao=self.role_fiscalizacao,
            role_geoinfra=self.role_geoinfra,
            role_drenagem=self.role_drenagem,
            role_usuarios=self.role_usuarios,
            role_tickets=self.role_tickets,
            role_cadastro_obra=self.role_cadastro_obra,
            role_selimp=self.role_selimp,
            role_compat=self.role_compat
        )
    
    def __repr__(self):
        return f"UserDynamoDto(name={self.name}, email={self.email}, user_id={self.user_id}, enabled={self.enabled}, department={self.department}, role_dashboards={self.role_dashboards}, role_fiscalizacao={self.role_fiscalizacao}, role_geoinfra={self.role_geoinfra}, role_drenagem={self.role_drenagem}, role_usuarios={self.role_usuarios}, role_tickets={self.role_tickets}, role_cadastro_obra={self.role_cadastro_obra}, role_selimp={self.role_selimp}, role_compat={self.role_compat})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__