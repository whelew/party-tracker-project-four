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
        self.character = Character.objects.create(
            name='Gandalf',
            character_class = 'wizard',
            health = 50,
            strength = 18,
            dexterity = 14,
            constitution = 20,
            intelligence = 20,
            wisdom = 20,
            charisma = 20,
            campaign=self.campaign
            )
        self.inventory = Inventory.objects.get(character=self.character)
        login_success = self.client.login(username='test', password='password123')
        self.assertTrue(login_success)

    # Test to retrieve and render only users campaign
    def test_campaign_list(self):
        url = reverse('campaign_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('campaign/campaign.html')
    
    # Test get create campaign request
    def create_campaign_get(self):
        url = reverse('create_campaign')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('campaign/create_campaign.html')

    # Test post create campaign request
    def create_campaign_post(self):
        url = reverse('create_campaign')
        campaign_data = {
            'name':'Test Campaign 2',
            'description':'This is my second test campaign'
        }
        response = self.client.post(url, campaign_data)
        current_campaign = Campaign.objects.get(name='Test Campaign 2')
        self.assertEqual(current_campaign.name, 'Test Campaign 2')
        self.assertEqual(current_campaign.description, 'This is my second test campaign')
        self.assertRedirects(response, url)

    # Test to see if campaign info contains campaign info and all characters
    def test_campaign_info(self):
        url = reverse('campaign_info', kwargs ={'pk': self.campaign.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('campaign/campaign_info.html')
        current_campaign = Campaign.objects.get(pk=self.campaign.id, user=self.user)
        self.assertEqual(current_campaign.name, 'Testcampaign')
        self.assertEqual(current_campaign.description, 'This is a test')
        self.assertEqual(self.character.name, 'Gandalf')
        self.assertIn('characters', response.context)
        self.assertEqual(len(response.context['characters']), 1)

    # Test campaign info when campaign has no characters
    def test_campaign_info_no_characters(self):
        # Create campaign without any characters
        empty_campaign = Campaign.objects.create(name = 'Empty', description = 'No characters', user=self.user)
        url = reverse('campaign_info', kwargs ={'pk': empty_campaign.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('campaign/campaign_info.html')
        self.assertIn('characters', response.context)
        self.assertEqual(len(response.context['characters']), 0)

    
    # Test create character get
    def test_create_character_get(self):
        url = reverse('create_character', kwargs={'campaign_id':self.campaign.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('campaign/create_character.html')


    # Test create character post
    def test_create_character_post(self):
        url = reverse('create_character', kwargs={'campaign_id':self.campaign.id})
        character_data = {
            'name':'Gimli',
            'character_class':'fighter',
            'health':50,
            'strength':20,
            'dexterity':10,
            'constitution':20,
            'intelligence':10,
            'wisdom':18,
            'charisma':20,
            'campaign':self.campaign.id
        }
        response = self.client.post(url, character_data)
        current_characters = Character.objects.filter(campaign_id=self.campaign).last()
        self.assertEqual(current_characters.name, 'Gimli')
        self.assertEqual(current_characters.strength, 20)
        self.assertEqual(current_characters.character_class, 'fighter')
        self.assertRedirects(response, reverse('campaign_info', kwargs = {'pk':self.campaign.id}))

    # Test for deleting a campaign from db get request
    def test_delete_campaign_get(self):
        url = reverse('delete_campaign', kwargs={'campaign_id':self.campaign.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['campaign'], self.campaign)
        self.assertTemplateUsed('campaign/confirm_delete.html')
    
    # Test for deleting a campaign post request
    def test_delete_campaign_post(self):
        url = reverse('delete_campaign', kwargs={'campaign_id':self.campaign.id})
        response = self.client.post(url)

        with self.assertRaises(Campaign.DoesNotExist):
            Campaign.objects.get(id=self.campaign.id)
        
        self.assertRedirects(response, reverse('campaign_list'))


    # Test for deleting a character get request
    def test_delete_character_get(self):
        url = reverse('delete_character', kwargs={'character_id':self.character.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['character'], self.character)
        self.assertTemplateUsed('campaign/confirm_delete_character.html')

    # Test for deleting a character post request
    def test_delete_character_post(self):
        url = reverse('delete_character', kwargs={'character_id':self.character.id})
        response = self.client.post(url)

        with self.assertRaises(Character.DoesNotExist):
            Character.objects.get(id=self.character.id)

        self.assertRedirects(response, reverse('campaign_info', kwargs={'pk':self.campaign.id}))

    # Test increment character stats post request
    def test_increment_character_stat_post(self):
        for action, expected_value in [('increment', 51), ('decrement', 50)]:
            url = reverse('update_character_stat', 
                kwargs={
                    'character_id': self.character.id,
                    'attribute': 'health',
                    'action': action
                    })
            response = self.client.post(url)
            self.character.refresh_from_db()
            self.assertEqual(self.character.health, expected_value)
            self.assertRedirects(response, reverse('campaign_info', kwargs={'pk':self.campaign.id}))

