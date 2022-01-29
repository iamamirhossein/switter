from django.contrib import admin
from account.models import Profile


# Register your models here.

class AdminProfile(admin.ModelAdmin):
    list_display = ['user', 'bio', 'is_private',]
    list_filter = ['user']


admin.site.register(Profile, AdminProfile)
