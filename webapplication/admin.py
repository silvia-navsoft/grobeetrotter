from django.contrib import admin
from .profiles.models import *
# Register your models here.

admin.site.register(User)
admin.site.register(UserType)
