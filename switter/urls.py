from django.urls import path, reverse
from . import views

app_name = "switter"

urlpatterns = [
    path('', views.home, name="home"),
    path('sweet/drafts', views.drafts, name="drafts"),
    path('sweet/create/', views.SweetCreateView.as_view(), name='sweet_create'),
    path('sweet/<int:pk>/delete', views.SweetDeleteView.as_view(), name='sweet_delete'),
    path('sweet/<int:pk>', views.SweetDetailView.as_view(), name='sweet_detail'),
]
