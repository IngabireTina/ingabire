from django.db import models
from stageproj2 import settings

from account.models import User


# Create your models here.

class Stock(models.Model):
    CATEGORY = [
        ('Computer Laptop', 'Computer Laptop'),
        ('Computer Desktop', 'Computer Desktop'),
        ('4G Router', '4G Router'),
        ('Printer', 'Printer'),
        ('Scanner', 'Scanner'),
        ('Television', 'Television'),
        ('Decoder', 'Decoder'),

    ]
    name = models.CharField(max_length=200, null=True)
    serialNumber = models.CharField(max_length=200, unique=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    code = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    quantity = models.IntegerField(default=None)

    def __str__(self):
        return self.name


class Item(models.Model):
    STATUS = [
        ('Work', 'Work'),
        ('Not Work', 'Not Work'),
        ('Submitted', 'Submitted'),

    ]

    device = models.ForeignKey(Stock, max_length=200, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, null=True, choices=STATUS, default='work')
    description = models.TextField(max_length=1000, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    person = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.device.name


