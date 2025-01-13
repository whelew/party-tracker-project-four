from . import views
from django.urls import path

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('character/<int:character_id>/inventory',
         views.add_item_to_inventory, name='add_item_to_inventory'),
    path('inventory/item/<int:inventory_item_id>/confirm_delete_item',
         views.delete_item, name='delete_item'),
]
