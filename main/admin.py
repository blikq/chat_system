from django.contrib import admin
from .models import DumUser, DumMsg

# Register your models here.
admin.site.register(DumUser)
admin.site.register(DumMsg)