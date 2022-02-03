from django.contrib import admin
from account.models import Profile
from django.contrib.auth.models import User


# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name',]
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


# Register your models here.

class AdminProfile(admin.ModelAdmin):
    list_display = ['user', 'complete_name', 'is_active', 'is_private']
    list_filter = ['user', 'is_active']


admin.site.register(Profile, AdminProfile)
