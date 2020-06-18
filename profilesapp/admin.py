from django.contrib import admin
from .models import UserProfile, Favourite
# Register your models here.


admin.site.register(UserProfile)
admin.site.register(Favourite)