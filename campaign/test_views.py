from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CampaignForm, CharacterForm
from item.models import Item, Inventory, InventoryItem
from .models import Campaign, Character


class CampaignTest(TestCase):
    # Set up instance of user with a campaign, character and inventory
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='password123', email='test@test.com')
        self.campaign = Campaign.objects.create(name='Testcampaign', description='This is a test', user=self.user)
        self.character = Character.objects.create(name='Gandalf', campaign=self.campaign)
        self.inventory = Inventory.objects.get(character=self.character)
        login_success = self.client.login(username='test', password='password123')
        self.assertTrue(login_success)

    # Test to retrieve and render only users campaign
    def test_campaign_list(self):
        url = reverse('campaign_info', kwargs ={'pk': self.campaign.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('campaign/campaign.html')
    
    def create_campaign_get(self):
        url = reverse('create_campaign')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('campaign/create_campaign.html')

    def create_campaign_post(self):
        url = reverse('create_campaign')
        form_data = {
            'name':'Test Campaign 2',
            'description':'This is my second test campaign'
        }
        response = self.client.post(url, form_data)
        current_campaign = Campaign.objects.get(name='Test Campaign 2')
        self.assertEqual(current_campaign.name, 'Test Campaign 2')
        self.assertEqual(current_campaign.description, 'This is my second test campaign')
        self.assertRedirects(response, url)

