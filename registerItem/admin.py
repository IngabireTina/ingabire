from django.contrib import admin
from registerItem.models import *
from account.models import User

# Register your models here.
admin.site.register(Item)
admin.site.register(Stock)


