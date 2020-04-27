"""Desctibe Accounts models."""

from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import TimeStampedModel
from users.models import User


class Account(TimeStampedModel):
    """Account model."""

    number = models.CharField(max_length=16, unique=True)
    is_debit = models.BooleanField(default=True)
    CVV = models.IntegerField()
    pincode = models.IntegerField()
    expiration_date = models.DateField()
    amount = models.FloatField(null=True)
    credit_limit = models.FloatField(null=True)
    deposit_amount = models.FloatField(null=True)
    credit_percentage = models.FloatField(null=True)
    deposit_percentage = models.FloatField(null=True)
    credit_start_date = models.DateTimeField(null=True)
    credit_end_date = models.DateTimeField(null=True)
    deposit_start_date = models.DateTimeField(null=True)
    deposit_end_date = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Transaction(TimeStampedModel):
    """Transaction model."""

    class TypeOfExpenceChoices(models.TextChoices):
        """Describes choices for the Transaction model."""

        ONLINE_PAYMENT = 'ON_PT', _('Online Payment')
        PAYMENT = 'PT', _('Payment')
        TRANSACTION_TO_ANOTHER_USER = 'TR_USR', _('Transaction to another user')
        UTILITY_PAYMENTS = 'UT_PT', _('Utility payments')

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    type_of_expence = models.CharField(
        max_length=6,
        choices=TypeOfExpenceChoices.choices,
        default=TypeOfExpenceChoices.PAYMENT
    )
    amount = models.FloatField()
    receiver = models.CharField(max_length=16)


class Company(TimeStampedModel):
    """Company model."""

    company_name = models.CharField(max_length=25, unique=True)
    company_owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    email = models.EmailField(max_length=70, unique=True)
    amount = models.FloatField(null=True)
    reg_location = models.CharField(max_length=25, null=True)
    account = models.OneToOneField(Account, on_delete=models.DO_NOTHING)
