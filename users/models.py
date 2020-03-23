from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=70, unique=True)
    phone_number = models.CharField(max_length=13, unique=True)
    passport_number = models.CharField(max_length=8, unique=True)
    identity_code = models.CharField(max_length=15, unique=True)
    company = models.ForeignKey("self", on_delete=models.CASCADE)
    salary = models.FloatField()
    birth_date = models.DateField()
    residence_permit = models.TextField(max_length=255)


class Roles(models.Model):
    role_name = models.IntegerField()
    user = models.OneToOneField(Users, on_delete=models.CASCADE)

