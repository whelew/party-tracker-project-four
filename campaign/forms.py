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
            'constitution', 'intelligence', 'wisdom', 'charisma', 'campaign',
        ]
    
    def __init__(self, *args, **kwargs):
        # Capture user instance passed from the view
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        # Filter campaigns only belonging to loggedin user
        if user:
            self.fields['campaign'].queryset = Campaign.objects.filter(user=user)