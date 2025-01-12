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

        for attribute in ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']:
            invalid_attr = character_data.copy()
            invalid_attr[attribute] = 21
            form = CharacterForm(data=invalid_attr)
            self.assertFalse(form.is_valid(), msg=f'Form Is Not Valid {attribute} is higher than 20')
            invalid_attr[attribute] = 0
            form = CharacterForm(data=invalid_attr)
            self.assertFalse(form.is_valid(), msg=f'Form Is Not Valid when {attribute} is lower than 1')
        
        for field in ['name', 'character_class', 'health', 'strength', 
                      'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']:
            invalid_fields = character_data.copy()
            invalid_fields[field] = ''
            form = CharacterForm(data=invalid_fields)
            self.assertFalse(form.is_valid(), msg=f'Form Is Not Valid {field} is empty')

        