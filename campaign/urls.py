from . import views
from django.urls import path

urlpatterns = [
    path('', views.campaign_list, name='campaign_list'),
    path('newcampaign/', views.create_campaign, name='create_campaign'),
    path('<int:pk>/', views.campaign_info, name='campaign_info'),
    path('<int:pk>/create_character', views.create_character, name='create_character')
]