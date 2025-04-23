
from rest_framework.response import Response
from rest_framework import status


def api_response_data (message, status_code, data=None):
    response_data = {
       "status_code" : status_code,
       "message" : {
           "title" : "Success" if status_code == 6000 else "Failed",
           "body" : message,
           "description": message
            if status_code == 6000
            else "Sorry, An error occured",
       },
    }

    if not data is None:
        response_data["data"] = data

    if status_code == 6000:
        return Response(response_data, status=status.HTTP_200_OK)
    elif status_code == 6001:
        return Response(response_data, status=status.HTTP_200_OK)
    elif status_code == 6002:
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(response_data, status=status.HTTP_202_ACCEPTED)
    