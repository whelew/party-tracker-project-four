from django.contrib.auth.models import User
from django.test import TestCase
from .forms import CampaignForm, CharacterForm
from .models import Campaign, Character

class TestCampaignForm(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='password123', email='test@test.com')
    
    def test_if_form_is_valid(self):
        """ Test if form is valid with correct data """

        campaign_data = {
            'name': 'campaign three',
            'description': 'description of test'
        } 

        form = CampaignForm(data=campaign_data)

        self.assertTrue(form.is_valid(), msg='This form is valid')

    def test_if_form_is_invalid(self):
        """ Test with incorrect name """

        campaign_data = {
            'name': '',
            'description': 'description of test'
        } 

        form = CampaignForm(data=campaign_data)

        self.assertFalse(form.is_valid(), msg='This is not valid')
    
    def test_if_form_has_empty_description(self):
        """ Test with empty description """

        campaign_data = {
            'name': 'Test 3',
            'description': ''
        } 

        form = CampaignForm(data=campaign_data)

        self.assertTrue(form.is_valid(), msg='This form is valid')

class TestCharacterForm(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='password123', email='test@test.com')
        self.campaign = Campaign.objects.create(name='Testcampaign4', description='This is test four', user=self.user)

    def test_if_data_is_valid(self):
        character_data = {
            'name': 'Aragorn',
            'character_class': 'paladin',
            'health': '50',
            'strength': '20',
            'dexterity': '19',
            'constitution': '20',
            'intelligence': '18',
            'wisdom': '20',
            'charisma': '20',
        }

        form = CharacterForm(data=character_data)

        self.assertTrue(form.is_valid(), msg='Form Is Valid')

    def test_if_data_is_invalid(self):
        """ Test if strength stat is over validator max 20"""
        character_data = {
            'name': 'Aragorn',
            'character_class': 'paladin',
            'health': '50',
            'strength': '21',
            'dexterity': '19',
            'constitution': '20',
            'intelligence': '18',
            'wisdom': '20',
            'charisma': '20',
        }

        form = CharacterForm(data=character_data)

        self.assertFalse(form.is_valid(), msg='Form Is Not Valid')
        