__all__ = [
    "Account"
]
from django.db import models
from .base import BaseModel
from app.accounts.managers.account import AccountManager
from uuid import uuid4


class Account(BaseModel):
    """
    Account is a user account
    """
    account_id = models.CharField(
        default=uuid4, max_length=128, unique=True, null=True, blank=True)
    customer = models.ForeignKey(
        'customer.Customer', on_delete=models.CASCADE)
    account_number = models.CharField(max_length=128, null=True, blank=True)
    balance = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)

    objects = AccountManager()

    def __str__(self):
        return f'{self.__class__.__name__} ID:{self.id} {self.name}'

    def deposit(self, amount):
        """ Deposit money to account """
        self.balance += amount
        return self.save()

    def withdraw(self, amount):
        """ Withdraw money from account """
        self.balance -= amount
        return self.save()

    def get_balance(self):
        """ Get account balance """
        return self.balance
