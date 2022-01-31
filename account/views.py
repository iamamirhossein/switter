from django.shortcuts import render
from django.views.generic import ListView
from .models import Profile


class ProfileListView(ListView):
    model = Profile
    paginate_by = 10
    template_name = 'switter/profiles.html'

    def get_queryset(self):
        return Profile.objects.filter(is_active=True)
