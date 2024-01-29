from typing import Optional
from src.shared.domain.entities.user import User

class UserViewmodel:
    user_id: str
    email: str
    name: str
    department: str
    role_dashboards: bool = None
    role_fiscalizacao: bool = None
    role_geoinfra: bool = None
    role_drenagem: bool = None
    role_usuarios: bool = None
    role_tickets: bool = None
    role_cadastro_obra: bool = None
    role_selimp: bool = None
    role_compat: bool = None
    enabled: str

    def __init__(self, user: User):
        self.user_id = user.user_id
        self.email = user.email
        self.name = user.name
        self.department = user.department
        self.role_dashboards = user.role_dashboards
        self.role_fiscalizacao = user.role_fiscalizacao
        self.role_geoinfra = user.role_geoinfra
        self.role_drenagem = user.role_drenagem
        self.role_usuarios = user.role_usuarios
        self.role_tickets = user.role_tickets
        self.role_cadastro_obra = user.role_cadastro_obra
        self.role_selimp = user.role_selimp
        self.role_compat = user.role_compat
        self.enabled = user.enabled

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'email': self.email,
            'name': self.name,
            'department': self.department,
            'enabled': self.enabled,
            'role_dashboards': self.role_dashboards ,
            'role_fiscalizacao': self.role_fiscalizacao,
            'role_geoinfra': self.role_geoinfra,
            'role_drenagem': self.role_drenagem,
            'role_usuarios': self.role_usuarios,
            'role_tickets': self.role_tickets,
            'role_cadastro_obra': self.role_cadastro_obra,
            'role_selimp': self.role_selimp,
            'role_compat': self.role_compat,
        }
    
class UpdateUserViewmodel:
    user: UserViewmodel

    def __init__(self, user: User):
        self.user = UserViewmodel(user=user)

    def to_dict(self):
        return {
            'user': self.user.to_dict(),
            'message': 'Usuário atualizado com sucesso!'
        }