from django.urls import path, reverse
from . import views

app_name = "switter"

urlpatterns = [
    path('', views.home, name="home"),
    path('sweet/drafts', views.drafts, name="drafts"),
    path('sweet/create/', views.SweetCreateView.as_view(), name='sweet_create'),
    path('sweet/delete/<int:pk>', views.SweetDeleteView.as_view(), name='sweet_delete'),
]
