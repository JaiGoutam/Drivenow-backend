from abstract.response import response_wrapper
from abstract.validate_request import validate_request
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from rest_framework import permissions, status
from django.contrib.auth import get_user_model
import traceback

User = get_user_model()

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    @response_wrapper
    def post(self, request, response):
        validate_request(
            {
                "email": "Email",
                "password": "Password",
                "full_name": "Full Name"
            },
            request.data,
        )
        api_status, message, data = status.HTTP_200_OK, "", {}

        try:
            email = request.data.get("email")
            password = request.data.get("password")
            full_name = request.data.get("full_name")
            phone = request.data.get("phone")

            if User.objects.filter(email=email).exists():
                message = "User already exists with this email."
                api_status = status.HTTP_400_BAD_REQUEST
            else:
                user = User.objects.create(
                    email=email,
                    full_name=full_name,
                    phone=phone,
                    password=make_password(password),
                )
                data = {"id": user.id, "email": user.email}
                message = "User registered successfully."
                api_status = status.HTTP_201_CREATED

        except Exception:
            print(traceback.format_exc())
            message = "Something went wrong during registration."
            api_status = status.HTTP_500_INTERNAL_SERVER_ERROR

        response.data, response.message, response.status = data, message, api_status
