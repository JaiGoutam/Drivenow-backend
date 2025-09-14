from rest_frameworks_simplejwt.views import *
from booking.views import *
from django.urls import re_path

urlpatterns = [
    re_path(r"^check/$", TokenVerifyView.as_view(), name="token_refresh")
]