from django.db import models

from users.models import Users


class Account(models.Model):
    number = models.CharField(max_length=16, unique=True)
    is_debit = models.BooleanField()
    CVV = models.IntegerField()
    pincode = models.IntegerField()
    expiration_date = models.DateField()
    amount = models.FloatField()
    credit_limit = models.FloatField()
    deposit_amount = models.FloatField()
    credit_percentage = models.FloatField()
    deposit_percentage = models.FloatField()
    credit_start_date = models.DateTimeField()
    credit_end_date = models.DateTimeField()
    deposit_start_date = models.DateTimeField()
    deposit_end_date = models.DateTimeField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)


class Transactions(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    type_of_expence = models.CharField(max_length=50)
    amount = models.FloatField()
    receiver = models.CharField(max_length=16)
