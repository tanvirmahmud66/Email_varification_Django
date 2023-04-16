from django.contrib import admin
from .models import Profile
# Register your models here.


class ProfileAdminView(admin.ModelAdmin):
    list_display = ('user', 'token', 'is_varified')


admin.site.register(Profile, ProfileAdminView)
