from django.contrib import admin

from .models import Users, Events

admin.site.register(Users)
admin.site.register(Events)