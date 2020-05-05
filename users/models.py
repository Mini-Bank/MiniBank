"""Desctibe User models."""

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from common.models import TimeStampedModel


class Role(TimeStampedModel):
    """Role model."""

    role_name = models.IntegerField()


class User(TimeStampedModel, AbstractBaseUser):
    """User model."""

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=70, unique=True)
    phone_number = models.CharField(max_length=13, unique=True)
    passport_number = models.CharField(max_length=8, unique=True)
    identity_code = models.CharField(max_length=15, unique=True)
    salary = models.FloatField()
    birth_date = models.DateField()
    residence_permit = models.TextField(max_length=255)
    password = models.CharField(max_length=88)
    role = models.OneToOneField(Role, on_delete=models.DO_NOTHING)
    user_company = models.ForeignKey("accounts.Company", on_delete=models.DO_NOTHING, blank=True)
