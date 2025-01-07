from django import forms
from .models import Item, Inventory, InventoryItem

class AddItemForm(forms.Form):
    # Allow user to select an item and quantity of item.
    item = forms.ModelChoiceField(queryset=Item.objects.all(), label="Select Item")
    quantity = forms.IntegerField(min_value=1, label='Quantity')

