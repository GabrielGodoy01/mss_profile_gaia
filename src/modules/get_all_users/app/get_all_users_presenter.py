
from .get_all_users_controller import GetAllUsersController
from .get_all_users_usecase import GetAllUsersUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo = repo = Environments.get_user_repo()()
usecase = GetAllUsersUsecase(repo)
controller = GetAllUsersController(usecase)

def get_all_users_presenter(event, context):

    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()

def lambda_handler(event, context):
    response = get_all_users_presenter(event, context)
    
    return response