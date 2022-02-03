from django.shortcuts import get_object_or_404
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
    queryset = Profile.objects.filter(is_active=True).annotate(slug=F('user__username'))
    template_name = 'switter/profile.html'

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(self.queryset, slug=slug)

    def post(self, request, *args, **kwargs):
        current_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_profile.follows.add(self.get_object())
        elif action == "unfollow":
            current_profile.follows.remove(self.get_object())
        current_profile.save()
        context = {
            "object": self.get_object()
        }
        return self.render_to_response(context=context)
