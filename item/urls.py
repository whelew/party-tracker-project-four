from . import views
from django.urls import path

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('character_inventory', views.add_item_to_inventory, name='add_item_to_inventory'),
]