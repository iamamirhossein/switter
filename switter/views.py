from django.shortcuts import render
from .forms import SweetForm


def home(request):
    form = SweetForm
    return render(request, "switter/dashboard.html", {"form": form})
