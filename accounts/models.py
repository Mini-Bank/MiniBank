from django.db import models

from common.models import TimeStampedModel
from users.models import Users


class Account(TimeStampedModel):
    number = models.CharField(max_length=16, unique=True)
    is_debit = models.BooleanField(default=True)
    CVV = models.IntegerField()
    pincode = models.IntegerField()
    expiration_date = models.DateField()
    amount = models.FloatField()
    credit_limit = models.FloatField(null=True)
    deposit_amount = models.FloatField(null=True)
    credit_percentage = models.FloatField()
    deposit_percentage = models.FloatField()
    credit_start_date = models.DateTimeField()
    credit_end_date = models.DateTimeField()
    deposit_start_date = models.DateTimeField()
    deposit_end_date = models.DateTimeField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)


class Transaction(TimeStampedModel):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    type_of_expence = models.CharField(max_length=50)
    amount = models.FloatField()
    receiver = models.CharField(max_length=16)
