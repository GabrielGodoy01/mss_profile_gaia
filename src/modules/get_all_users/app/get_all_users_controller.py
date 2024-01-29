from .get_all_users_usecase import GetAllUsersUsecase
from .get_all_users_viewmodel import GetAllUsersViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, InvalidTokenError, NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import BadRequest, Forbidden, InternalServerError, NotFound, Unauthorized, OK


class GetAllUsersController:
    def __init__(self, usecase: GetAllUsersUsecase):
        self.getAllUsersUsecase = usecase
    
    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('user_id') is None:
                raise MissingParameters('user_id')

            user_list = self.getAllUsersUsecase(user_id=request.data.get('user_id'))

            viewmodel = GetAllUsersViewmodel(user_list)

            return OK(viewmodel.to_dict())
        
        except NoItemsFound as err:
            return NotFound(body={"message": f'{err.message}'})

        except MissingParameters as err:
            return BadRequest(body={"message": f"Parâmetro ausente: {err.message}"})

        except ForbiddenAction as err:
            return Forbidden(body={"message": f"Usuário não autorizado"})

        except InvalidTokenError as e:
            return Unauthorized(body={"message": "Token inválido ou expirado"})

        except EntityError as err:
            return BadRequest(body={"message": f'Parâmetro inválido: {err.message}'})

        except Exception as err:
            return InternalServerError(body={"message": err.args[0]})
