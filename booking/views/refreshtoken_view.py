from rest_framework_simplejwt.views import TokenRefreshView
from booking.models import UserSessions
from rest_framework import status
from abstract.response import response_wrapper
from abstract.validate_request import validate_request
import traceback

class CustomTokenRefreshView(TokenRefreshView):
    @response_wrapper
    def post(self, request, response):
        validate_request({"refresh": "Refresh Token"}, request.data)
        api_status, message, data = status.HTTP_200_OK, "", {}

        try:
            old_refresh = request.data.get("refresh")
            res = super().post(request)
            if res.status_code == 200:
                data = res.data
                message = "Token refreshed successfully."
                new_refresh = res.data.get("refresh")
                if new_refresh:
                    UserSessions.objects.filter(refresh_token=old_refresh).update(refresh_token=new_refresh)
                api_status = status.HTTP_200_OK
            else:
                message = "Refresh failed."
                api_status = res.status_code

        except Exception:
            print(traceback.format_exc())
            message = "Something went wrong during token refresh."
            api_status = status.HTTP_500_INTERNAL_SERVER_ERROR

        response.data, response.message, response.status = data, message, api_status
