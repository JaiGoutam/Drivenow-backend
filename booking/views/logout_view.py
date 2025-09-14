from rest_framework_simplejwt.tokens import RefreshToken
from booking.models import UserSessions
from rest_framework.views import APIView
from rest_framework import status, permissions
from abstract.response import response_wrapper
from abstract.validate_request import validate_request
import traceback

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @response_wrapper
    def post(self, request, response):
        validate_request({"refresh": "Refresh Token"}, request.data)
        api_status, message, data = status.HTTP_200_OK, "", {}

        try:
            refresh_token = request.data.get("refresh")

            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
            except Exception:
                pass  # already invalid or blacklisted

            UserSessions.objects.filter(refresh_token=refresh_token).update(is_active=False)
            message = "Logout successful."
            api_status = status.HTTP_200_OK

        except Exception:
            print(traceback.format_exc())
            message = "Logout failed."
            api_status = status.HTTP_500_INTERNAL_SERVER_ERROR

        response.data, response.message, response.status = data, message, api_status
