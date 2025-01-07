from . import views
from django.urls import path

urlpatterns = [
    path('', views.campaign_list, name='campaign_list'),
    path('newcampaign/', views.create_campaign, name='create_campaign'),
    path('<int:pk>/', views.campaign_info, name='campaign_info'),
    path('<int:campaign_id>/create_character/', views.create_character, name='create_character'),
    path('<int:campaign_id>/confirm_delete/', views.delete_campaign, name='delete_campaign'),
    path('character/<int:character_id>/confirm_delete_character/', views.delete_character, name='delete_character'),
    path('character/<int:character_id>/stat/<str:attribute>/<str:action>', views.update_character_stat, name='update_character_stat')
]