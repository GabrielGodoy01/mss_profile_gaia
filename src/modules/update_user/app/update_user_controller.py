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
            
            if request.data.get('enabled') is None:
                raise MissingParameters('enabled')
            
            if request.data.get('role_dashboard_qualidade') is None:
                raise MissingParameters('role_dashboard_qualidade')
            
            if request.data.get('role_dashboard_deteccao') is None:
                raise MissingParameters('role_dashboard_deteccao')
            
            if request.data.get('role_dashboard_tempo') is None:
                raise MissingParameters('role_dashboard_tempo')
            
            if request.data.get('role_dashboard_geoinfra') is None:
                raise MissingParameters('role_dashboard_geoinfra')
            
            if request.data.get('role_dashboard_recapeamento') is None:
                raise MissingParameters('role_dashboard_recapeamento')
            
            if request.data.get('role_dashboard_anel_viario') is None:
                raise MissingParameters('role_dashboard_anel_viario')
            
            if request.data.get('role_dashboard_sist_unificado') is None:
                raise MissingParameters('role_dashboard_sist_unificado')
            
            if request.data.get('role_modfisc_convias') is None:
                raise MissingParameters('role_modfisc_convias')
            
            if request.data.get('role_modfisc_osmv') is None:
                raise MissingParameters('role_modfisc_osmv')
            
            if request.data.get('role_modfisc_osct') is None:
                raise MissingParameters('role_modfisc_osct')
            
            if request.data.get('role_modfisc_relatoriomv') is None:
                raise MissingParameters('role_modfisc_relatoriomv')
            
            if request.data.get('role_modfisc_vistoriapv') is None:
                raise MissingParameters('role_modfisc_vistoriapv')
            
            if request.data.get('role_modfisc_vistoriarecape') is None:
                raise MissingParameters('role_modfisc_vistoriarecape')
            
            if request.data.get('role_interf_mapa') is None:
                raise MissingParameters('role_interf_mapa')
            
            if request.data.get('role_interf_protproc') is None:
                raise MissingParameters('role_interf_protproc')
            
            if request.data.get('role_drenagem_ativos') is None:
                raise MissingParameters('role_drenagem_ativos')
            
            if request.data.get('role_drenagem_redes') is None:
                raise MissingParameters('role_drenagem_redes')
            
            if request.data.get('role_usuarios') is None:
                raise MissingParameters('role_usuarios')
            
            if request.data.get('role_tickets') is None:
                raise MissingParameters('role_tickets')
            
            

            user = self.UpdateUserUsecase(
                    new_user_data=User(
                        user_id=request.data.get('user_id'),
                        name=request.data.get('name'),
                        email=request.data.get('email'),
                        department=request.data.get('department'),
                        enabled=request.data.get('enabled'),
                        role_dashboard_qualidade=request.data.get('role_dashboard_qualidade'),
                        role_dashboard_deteccao=request.data.get('role_dashboard_deteccao'),
                        role_dashboard_tempo=request.data.get('role_dashboard_tempo'),
                        role_dashboard_geoinfra=request.data.get('role_dashboard_geoinfra'),
                        role_dashboard_recapeamento=request.data.get('role_dashboard_recapeamento'),
                        role_dashboard_anel_viario=request.data.get('role_dashboard_anel_viario'),
                        role_dashboard_sist_unificado=request.data.get('role_dashboard_sist_unificado'),
                        role_modfisc_convias=request.data.get('role_modfisc_convias'),
                        role_modfisc_osmv=request.data.get('role_modfisc_osmv'),
                        role_modfisc_osct=request.data.get('role_modfisc_osct'),
                        role_modfisc_relatoriomv=request.data.get('role_modfisc_relatoriomv'),
                        role_modfisc_vistoriapv=request.data.get('role_modfisc_vistoriapv'),
                        role_modfisc_vistoriarecape=request.data.get('role_modfisc_vistoriarecape'),
                        role_interf_mapa=request.data.get('role_interf_mapa'),
                        role_interf_protproc=request.data.get('role_interf_protproc'),
                        role_drenagem_ativos=request.data.get('role_drenagem_ativos'),
                        role_drenagem_redes=request.data.get('role_drenagem_redes'),
                        role_usuarios=request.data.get('role_usuarios'),
                        role_tickets=request.data.get('role_tickets')
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