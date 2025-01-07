from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Item, Inventory, InventoryItem

# Create your views here.


@login_required
def item_list(request):
    """
    Create a list of Items using Item Model
    """

    items = Item.objects.all()

    return render(
        request, 'item/item_list.html',
        {'items': items},
    )
