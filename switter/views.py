from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView
from .forms import SweetForm
from .models import Sweet
from .mixins import FieldsMixin, FormValidMixin, AuthorAccessMixin


def home(request):
    form = SweetForm
    return render(request, "switter/dashboard.html", {"form": form})


def drafts(request):
    return render(request, "switter/drafts.html")


class SweetCreateView(FieldsMixin, FormValidMixin, CreateView):
    model = Sweet
    success_url = reverse_lazy('switter:home')
    template_name = 'switter/dashboard.html'


class SweetDeleteView(AuthorAccessMixin, DeleteView):
    model = Sweet
    success_url = reverse_lazy('switter:drafts')


class SweetDetailView(AuthorAccessMixin, DetailView):
    model = Sweet
    template_name = 'switter/detail.html'

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.draft = False if instance.draft else True
        instance.save()
        context = {
            "object": self.get_object()
        }
        return self.render_to_response(context=context)

