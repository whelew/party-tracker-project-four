from . import views
from django.urls import path

urlpatterns = [
    path('campaign/', views.campaign_list, name='campaign_list'),
    path('newcampaign/', views.create_campaign, name='create_campaign'),
]