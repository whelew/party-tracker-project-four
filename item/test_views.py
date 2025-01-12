from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import AddItemForm
from .models import Item, Inventory, InventoryItem
from campaign.models import Campaign, Character


class ItemListTest(TestCase):
    def setUp(self):
        Item.objects.create(name='Rope', description='50m of Rope.')
        Item.objects.create(name='Fishing Rod', description='A device used for fishing.')
        Item.objects.create(name='Torch', description='A source of light when in the darkest of dungeons.')
       

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

class AddItemToInventory(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='password123', email='test@test.com')
        self.campaign = Campaign.objects.create(name='Testcampaign', description='This is a test', user=self.user)
        self.character = Character.objects.create(name='Gandalf', campaign=self.campaign)
        self.inventory = Inventory.objects.get(character=self.character)
        self.item = Item.objects.create(name='Rope', description='50m of Rope.')

    def test_add_item_get(self):
        self.client.login(username='test', password='password123')
        url = reverse('add_item_to_inventory', kwargs={'character_id': self.character.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'inventory/character_inventory.html')
        self.assertIn('form', response.context)
        self.assertIn('inventory', response.context)
        self.assertIn('inventory_items', response.context)

    def test_add_item_post(self):
        login_success = self.client.login(username='test', password='password123')
        self.assertTrue(login_success)
        url = reverse('add_item_to_inventory', kwargs={'character_id': self.character.id})
        form_data = {
            'item':self.item.id,
            'quantity': 2
        }
        response = self.client.post(url, form_data)
        inventory_item = InventoryItem.objects.get(inventory=self.inventory, item=self.item)
        self.assertEqual(inventory_item.quantity, 2)
        self.assertRedirects(response, url)
