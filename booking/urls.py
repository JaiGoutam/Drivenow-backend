from rest_framework_simplejwt.views import *
from booking.views import *
from django.urls import re_path
from django.urls import path


urlpatterns = [
    re_path(r"^auth/register/$", RegisterView.as_view(), name="register"),
    re_path(r"^auth/login/$", LoginView.as_view(), name="login"),
    re_path(r"^auth/logout/$", LogoutView.as_view(), name="logout"),
    re_path(r"^auth/refresh/$", CustomTokenRefreshView.as_view(), name="token_refresh"),
    re_path(r"^auth/verify/$", TokenVerifyView.as_view(), name="token_verify"),
]