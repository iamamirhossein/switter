from django.contrib import admin
from .models import Sweet, Fave


class SweetAdmin(admin.ModelAdmin):
    fields = ('user', 'body', 'draft', 're_sweet')
    list_display = ('user', 'draft', 'faves_count')


admin.site.register(Sweet, SweetAdmin)
admin.site.register(Fave)
