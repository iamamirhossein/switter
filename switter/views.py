from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from .forms import SweetForm
from .models import Sweet
from .mixins import FieldsMixin, FormValidMixin, AuthorAccessMixin


def home(request):
    form = SweetForm
    return render(request, "switter/dashboard.html", {"form": form})


def drafts(request):
    return render(request, "switter/drafts.html")


class SweetCreate(FieldsMixin, FormValidMixin, CreateView):
    model = Sweet
    success_url = reverse_lazy('switter:home')
    template_name = 'switter/dashboard.html'


class SweetDeleteView(AuthorAccessMixin, DeleteView):
    model = Sweet
    success_url = reverse_lazy('switter:home')
