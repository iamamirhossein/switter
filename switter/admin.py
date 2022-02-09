from django.contrib import admin
from .models import Sweet, Fave


class SweetAdmin(admin.ModelAdmin):
    fields = ('user', 'body', 'draft', 're_sweet')
    list_display = ('user', 'draft')


admin.site.register(Sweet, SweetAdmin)
