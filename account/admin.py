from django.contrib import admin
from account.models import Profile
from django.contrib.auth.models import User


# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'email']
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


# Register your models here.

class AdminProfile(admin.ModelAdmin):
    list_display = ['user', 'bio', 'is_private', ]
    list_filter = ['user']


admin.site.register(Profile, AdminProfile)
