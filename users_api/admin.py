from django.contrib import admin

# Register your models here.
from .models import User, Home, Photo
admin.site.register(User, Home, Photo)
