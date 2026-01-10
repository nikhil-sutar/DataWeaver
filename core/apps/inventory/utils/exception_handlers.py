from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc,context):
    response = exception_handler(exc,context)

    if response is None:
        return Response({
            "message":"Internal server error"
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    error_response = {
        "message":"Request failed",
        "errors":response.data
    }

    if response.status_code == 400:
        error_response["message"] = "Validation error"
    elif response.status_code == 404:
        error_response["message"] = "Resource not found"

    return Response(
        error_response,
        status=response.status_code
    )