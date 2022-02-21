from django.urls import path, reverse
from . import views

app_name = "switter"

urlpatterns = [
    path('', views.home, name="home"),
    path('sweet/create/', views.SweetCreate.as_view(), name='sweet_create'),
]
