from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from booking.models import UserSessions
from rest_framework.views import APIView
from rest_framework import status, permissions
from abstract.response import response_wrapper
from abstract.validate_request import validate_request
import traceback

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    @response_wrapper
    def post(self, request, response):
        validate_request({"email": "Email", "password": "Password"}, request.data)
        api_status, message, data = status.HTTP_200_OK, "", {}

        try:
            email, password = request.data.get("email"), request.data.get("password")
            user = authenticate(request, email=email, password=password)

            if not user:
                message = "Invalid email or password."
                api_status = status.HTTP_401_UNAUTHORIZED
            else:
                refresh = RefreshToken.for_user(user)
                access, refresh_token = str(refresh.access_token), str(refresh)

                UserSessions.objects.create(
                    user=user,
                    refresh_token=refresh_token,
                    user_agent=request.META.get("HTTP_USER_AGENT", ""),
                    ip_address=request.META.get("REMOTE_ADDR", "")
                )

                data = {"access": access, "refresh": refresh_token, "user_id": user.id, "email": user.email}
                message = "Login successful."
                api_status = status.HTTP_200_OK

        except Exception:
            print(traceback.format_exc())
            message = "Something went wrong during login."
            api_status = status.HTTP_500_INTERNAL_SERVER_ERROR

        response.data, response.message, response.status = data, message, api_status
