from django import forms
from .models import Campaign, Character

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['name', 'description']

class CharacterForm(forms.ModelForm):

    class Meta:
        model = Character
        fields = [
            'name', 'character_class', 'health', 'strength', 'dexterity', 
            'constitution', 'intelligence', 'wisdom', 'charisma',
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)