from . import views
from django.urls import path

urlpatterns = [
    path('', views.campaign_list, name='campaign_list'),
    path('campaign/', views.campaign_list, name='campaign_list'),
    path('home/', views.campaign_list, name='home'),
]