import abc
import re
from src.shared.helpers.errors.domain_errors import EntityError


class User(abc.ABC):
    user_id: str
    email: str
    name: str
    department: str = None
    role_dashboards: bool = None
    role_fiscalizacao: bool = None
    role_geoinfra: bool = None
    role_drenagem: bool = None
    role_usuarios: bool = None
    role_tickets: bool = None
    role_cadastro_obra: bool = None
    role_selimp: bool = None
    role_compat: bool = None
    enabled: bool

    MIN_NAME_LENGTH = 2
    USER_ID_LENGTH = 36

    def __init__(self, user_id: str, email: str, name: str,
            enabled: bool,
            department: str = None,
            role_dashboards: bool = None, 
            role_fiscalizacao: bool = None,
            role_geoinfra: bool = None,
            role_drenagem: bool = None,
            role_usuarios: bool = None,
            role_tickets: bool = None,
            role_cadastro_obra: bool = None,
            role_selimp: bool = None,
            role_compat: bool = None,
        ):

        if not User.validate_user_id(user_id):
            raise EntityError("user_id")
        self.user_id = user_id
        
        if not User.validate_email(email):
            raise EntityError("email")
        self.email = email

        if not User.validate_name(name):
            raise EntityError("name")
        self.name = name

        if department is not None:
            if type(department) != str:
                raise EntityError("department")
        self.department = department

        if role_dashboards is not None:
            if type(role_dashboards) != bool:
                raise EntityError("role_dashboards")
        self.role_dashboards = role_dashboards

        if role_fiscalizacao is not None:
            if type(role_fiscalizacao) != bool:
                raise EntityError("role_fiscalizacao")
        self.role_fiscalizacao = role_fiscalizacao

        if role_geoinfra is not None:
            if type(role_geoinfra) != bool:
                raise EntityError("role_geoinfra")
        self.role_geoinfra = role_geoinfra

        if role_drenagem is not None:
            if type(role_drenagem) != bool:
                raise EntityError("role_drenagem")
        self.role_drenagem = role_drenagem

        if role_usuarios is not None:
            if type(role_usuarios) != bool:
                raise EntityError("role_usuarios")
        self.role_usuarios = role_usuarios

        if role_tickets is not None:
            if type(role_tickets) != bool:
                raise EntityError("role_tickets")
        self.role_tickets = role_tickets

        if role_cadastro_obra is not None:
            if type(role_cadastro_obra) != bool:
                raise EntityError("role_cadastro_obra")
        self.role_cadastro_obra = role_cadastro_obra

        if role_selimp is not None:
            if type(role_selimp) != bool:
                raise EntityError("role_selimp")
        self.role_selimp = role_selimp

        if role_compat is not None:
            if type(role_compat) != bool:
                raise EntityError("role_compat")
        self.role_compat = role_compat

        if type(enabled) is not bool:
            raise EntityError("enabled")
        self.enabled = enabled



    @staticmethod
    def validate_email(email) -> bool:
        if email == None:
            return False
        elif type(email) != str:
            return False

        regex = re.compile(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

        return bool(re.fullmatch(regex, email))

    @staticmethod
    def validate_name(name: str) -> bool:
        regex = re.compile(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$")

        if name is None:
            return False
        elif type(name) != str:
            return False
        elif len(name) <= User.MIN_NAME_LENGTH:
            return False
        
        return bool(re.fullmatch(regex, name))

    @staticmethod
    def validate_user_id(user_id: str) -> bool:
        if type(user_id) != str:
            return False
        if len(user_id) != User.USER_ID_LENGTH:
            return False
        return True

    def to_dict(self) -> dict:
        return {
            'user_id': self.user_id,
            'email': self.email,
            'name': self.name,
            'department': self.department,
            'enabled': self.enabled,
            'role_dashboards': self.role_dashboards,
            'role_fiscalizacao': self.role_fiscalizacao,
            'role_geoinfra': self.role_geoinfra,
            'role_drenagem': self.role_drenagem,
            'role_usuarios': self.role_usuarios,
            'role_tickets': self.role_tickets,
            'role_cadastro_obra': self.role_cadastro_obra,
            'role_selimp': self.role_selimp,
            'role_compat': self.role_compat
        }
