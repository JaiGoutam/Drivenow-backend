# booking/models.py
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from datetime import datetime
from abstract.base_model import BaseModel  # your BaseModel from the code you pasted

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    full_name = models.CharField()
    email = models.CharField(unique=True)
    password_hash = models.CharField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    role = models.CharField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    r_status = models.CharField()
    is_active = models.BooleanField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"
