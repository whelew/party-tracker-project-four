from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item, Inventory, InventoryItem
from .forms import AddItemForm


def item_list(request):
    """
    Create a list of Items using Item Model
    """

    items = Item.objects.all()

    return render(
        request, 'item/item_list.html',
        {'items': items},
    )


@login_required
def add_item_to_inventory(request, character_id):
    """
    Add item to specific character invetory
    using character id to match correct character inventory
    """

    # Retrieve inventory belonging to specific character.
    inventory = get_object_or_404(
        Inventory,
        character__id=character_id,
        character__campaign__user=request.user)

    # Retrieve exsisting items in characters inventory.
    inventory_items = inventory.inventory_items.select_related('item')

    # Handles form request
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            item = form.cleaned_data['item']
            quantity = form.cleaned_data['quantity']

            # Check if item exsists in inventory.
            inventory_item, created = InventoryItem.objects.get_or_create(
                inventory=inventory,
                item=item,
                defaults={'quantity': quantity}
            )

            # Updates quantity of the item.
            if not created:
                inventory_item.quantity += quantity
                inventory_item.save()

            # Refresh form after adding item.
            return redirect('add_item_to_inventory', character_id=character_id)

    else:
        form = AddItemForm()

        # Render the form alongside inventory and current inventory items.
        return render(request, 'inventory/character_inventory.html', {
            'form': form,
            'inventory': inventory,
            'inventory_items': inventory_items,
            })


@login_required
def delete_item(request, inventory_item_id):
    """
    Allow a user to delete an item from their inventory.
    """
    inventory_item = get_object_or_404(
        InventoryItem,
        id=inventory_item_id,
        inventory__character__campaign__user=request.user
    )

    if request.method == 'POST':
        inventory_item.delete()
        return redirect('add_item_to_inventory',
                        character_id=inventory_item.inventory.character.id)
