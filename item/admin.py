from django.contrib import admin
from .models import Inventory, InventoryItem, Item

# Register your models here.
admin.site.register(Inventory)
admin.site.register(InventoryItem)
admin.site.register(Item)
