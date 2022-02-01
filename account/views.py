from django.db.models import F
from django.views.generic import ListView, DetailView
from .models import Profile


class ProfileListView(ListView):
    model = Profile
    paginate_by = 10
    template_name = 'switter/profiles.html'

    def get_queryset(self):
        return Profile.objects.filter(is_active=True)


class ProfileView(DetailView):
    model = Profile
    queryset = Profile.objects.filter(is_active=True)
    template_name = 'switter/profile.html'

    def get_queryset(self):
        return self.queryset.annotate(slug=F('user__username')).filter()

