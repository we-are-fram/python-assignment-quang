__all__ = ['Customer']

from django.db import models


class Customer(models.Model):
    """ Customer is a user account """

    name = models.CharField(max_length=128, unique=True,
                            null=False, blank=False)
    customer_id = models.CharField(
        max_length=128, unique=True, null=True, blank=True)
    email = models.EmailField(
        max_length=128, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f'{self.__class__.__name__} ID:{self.id} {self.name}'
