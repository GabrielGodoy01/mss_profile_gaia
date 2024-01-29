from src.shared.domain.entities.user import User
from .update_user_usecase import UpdateUserUsecase
from .update_user_viewmodel import UpdateUserViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, InvalidCredentials, InvalidTokenError, NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError, Forbidden, Unauthorized


class UpdateUserController:

    def __init__(self, usecase: UpdateUserUsecase):
        self.UpdateUserUsecase = usecase
    
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('user_id') is None:
                raise MissingParameters('user_id')
            
            if request.data.get('email') is None:
                raise MissingParameters('email')
            
            if request.data.get('name') is None:
                raise MissingParameters('name')
            
            if request.data.get('department') is None:
                raise MissingParameters('department')
            
            if request.data.get('role_dashboards') is None:
                raise MissingParameters('role_dashboards')
            
            if request.data.get('role_fiscalizacao') is None:
                raise MissingParameters('role_fiscalizacao')
            
            if request.data.get('role_geoinfra') is None:
                raise MissingParameters('role_geoinfra')
            
            if request.data.get('role_drenagem') is None:
                raise MissingParameters('role_drenagem')
            
            if request.data.get('role_usuarios') is None:
                raise MissingParameters('role_usuarios')
            
            if request.data.get('role_tickets') is None:
                raise MissingParameters('role_tickets')
            
            if request.data.get('role_cadastro_obra') is None:
                raise MissingParameters('role_cadastro_obra')
            
            if request.data.get('role_selimp') is None:
                raise MissingParameters('role_selimp')
            
            if request.data.get('role_compat') is None:
                raise MissingParameters('role_compat')
            
            if request.data.get('enabled') is None:
                raise MissingParameters('enabled')

            user = self.UpdateUserUsecase(
                    new_user_data=User(
                        user_id=request.data.get('user_id'),
                        name=request.data.get('name'),
                        email=request.data.get('email'),
                        department=request.data.get('department'),
                        role_dashboards=request.data.get('role_dashboards'),
                        role_fiscalizacao=request.data.get('role_fiscalizacao'),
                        role_geoinfra=request.data.get('role_geoinfra'),
                        role_drenagem=request.data.get('role_drenagem'),
                        role_usuarios=request.data.get('role_usuarios'),
                        role_tickets=request.data.get('role_tickets'),
                        role_cadastro_obra=request.data.get('role_cadastro_obra'),
                        role_selimp=request.data.get('role_selimp'),
                        role_compat=request.data.get('role_compat'),
                        enabled=request.data.get('enabled')
                    ),
                )
            
            viewmodel = UpdateUserViewmodel(user)
            response = OK(viewmodel.to_dict())

            return response
        
        except NoItemsFound as err:
            return NotFound(body={"message": 'Nenhum usuário encontrado' if err.message == "user" else f"Nenhum usuário encontrado com parâmetro: {err.message}"})

        except MissingParameters as err:
            return BadRequest(body={"message": f"Parâmetro ausente: {err.message}"})

        except EntityError as err:
            return BadRequest(body={"message": f"Parâmetro inválido: {err.message}"})

        except InvalidCredentials as err:
            return BadRequest(body={"message": f"Token inválido: {err.message}"})

        except ForbiddenAction as err:
            return Forbidden(body={"message": f"Ação não permitida: {err.message}"})

        except InvalidTokenError as e:
            return Unauthorized(body={"message": "Token inválido ou expirado"})
        
        except Exception as err:
            return InternalServerError(body={"message": err.args[0]})