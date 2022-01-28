from django.contrib import admin
from django.contrib.auth.models import User


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'email']


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
