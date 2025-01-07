from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item, Inventory, InventoryItem
from .forms import AddItemForm

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

@login_required
def add_item_to_inventory(request, character_id):
    """
    Add item to specific character invetory using character id to match correct character inventory
    """

    inventory = get_object_or_404(Inventory, character_id=character_id, character_user=request.user)

    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            item = form.cleaned_data['item']
            quantity = form.cleaned_data['quantity']

            # Check if item exsists in inventory.
            inventory_item, created = InventoryItem.objects.get_or_create(
                inventory = inventory,
                item=item,
                defaults={'quantity' : quantity}
            )

            # Updates quantity of the item.
            if not created:
                inventory_item.quantity += quantity
                inventory_item.save()
            
            return redirect('character_inventory', character_id=character_id)
        
        else:
            form = AddItemForm()
        
        return render(request, 'inventory/character_inventory', {'form' : form, 'inventory' : inventory})
    
