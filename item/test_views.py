from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import AddItemForm
from .models import Item, Inventory, InventoryItem


class ItemListTest(TestCase):
    def setUp(self):
        Item.objects.create(name="Rope", description="50m of Rope.")
        Item.objects.create(name="Fishing Rod", description="A device used for fishing.")
        Item.objects.create(name="Torch", description="A source of light when in the darkest of dungeons.")
       

    def test_item_library(self):
        url = reverse('item_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'item/item_list.html')
        self.assertIn('items', response.context)
        self.assertEqual(len(response.context['items']), 3)
        self.assertContains(response, 'Rope')
        self.assertContains(response, 'Fishing Rod')
        self.assertContains(response, 'Torch')
