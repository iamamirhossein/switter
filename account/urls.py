from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path('profiles/', views.ProfileListView.as_view(), name="profiles"),
    path('profile/<slug:slug>/', views.ProfileView.as_view(), name="profile-detail"),
]
