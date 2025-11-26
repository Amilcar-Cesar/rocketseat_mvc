from src.views.http_types.http_response import HttpResponse
from .error_types.http_bad_request import HttpBadRequestError
from .error_types.http_not_found import HttpNotFoundError 
from .error_types.http_unprocessable_entity import HttpUnprocessableEntiyError

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpBadRequestError, HttpNotFoundError, HttpUnprocessableEntiyError)):
        return HttpResponse(
            status_code=error.staus_code,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )
    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )
