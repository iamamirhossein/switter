from django.urls import path
from . import views

app_name = "switter"

urlpatterns = [
    path('', views.home, name="home"),
]