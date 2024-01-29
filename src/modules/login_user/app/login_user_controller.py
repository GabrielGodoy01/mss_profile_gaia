from .login_user_usecase import LoginUserUsecase
from .login_user_viewmodel import LoginUserViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import InvalidTokenError, NewPasswordRequired, NoItemsFound, ForbiddenAction, InvalidCredentials, UserNotConfirmed, UserNotValid
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import NotFound, BadRequest, InternalServerError, OK, Forbidden, \
    Unauthorized, UnauthorizedFirstLogin


class LoginUserController:

    def __init__(self, usecase: LoginUserUsecase):
        self.loginUserUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('user_id') is None:
                raise MissingParameters('user_id')
            
            if request.data.get('name') is None:
                raise MissingParameters('name')
            
            if request.data.get('email') is None:
                raise MissingParameters('email')
            
            if request.data.get('groups') is None:
                raise MissingParameters('groups')

            user = self.loginUserUsecase(user_id=request.data.get('user_id'), name=request.data.get('name'), email=request.data.get('email'), groups=request.data.get('groups'))
            login_user_viewmodel = LoginUserViewmodel(user=user)
            response = OK(login_user_viewmodel.to_dict())

            return response

        except NoItemsFound as err:
            return NotFound(body={"message": 'Nenhum usuário encontrado'})

        except ForbiddenAction as err:
            return Forbidden(body={"message": f"Ação não permitida: {err.message}"})

        except MissingParameters as err:
            return BadRequest(body={"message": f"Parâmetro ausente: {err.message}"})

        except EntityError as err:
            return BadRequest(body={"message": f"Parâmetro inválido: {err.message}"})

        except InvalidTokenError as err:
            return Unauthorized(body={"message": "Token inválido ou expirado"})
        
        except UserNotValid as err:
            return Unauthorized(body={"message": "Usuário inválido"})
        
        except InvalidCredentials as e:
            return Unauthorized(body={"message": "Credenciais inválidas"})

        except Exception as err:
            return InternalServerError(body={"message": err.args[0]})

