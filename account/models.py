from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Address(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    phone_number = models.CharField('phone_number', unique=True, max_length=200, null=True)
    address = models.ForeignKey(Address, max_length=200, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.username
