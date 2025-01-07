from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Campaign, Character
from .forms import CampaignForm, CharacterForm

# Create your views here.


@login_required
def campaign_list(request):
    """
    Display an individual :model:`campaign.Campaign`.

    **Context**

    ``monster``
        An instance of :model:`campaign.Campaign`.

    **Template:**

    :template:`campaign/campaign.html`
    """
     
    current_campaign = Campaign.objects.filter(user=request.user)

    return render(
        request, "campaign/campaign.html",
        {"current_campaign": current_campaign},
        )


@login_required
def create_campaign(request):
    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.user = request.user
            campaign.save()
            return redirect('campaign_list')
    else:
        form = CampaignForm()
    
    return render(request, 'campaign/create_campaign.html', {'form': form})


@login_required
def campaign_info(request, pk):
    """

    Display current campaign details.

    """
    campaign = get_object_or_404(Campaign, pk=pk, user=request.user)
    characters = campaign.characters.all() # Retrieve all characters linked to campaign id.

    return render(request, 'campaign/campaign_info.html', {'campaign' : campaign, 'characters' : characters})    


@login_required
def create_character(request, campaign_id):
    """
    Allow user to add characters to campaign based on campaign id.
    """
    campaign = get_object_or_404(Campaign, id=campaign_id, user=request.user)

    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            character.campaign = campaign # link the character to campaign/id
            character.save()
            return redirect('campaign_info', pk=campaign_id) 
    else:
        form = CharacterForm()
    
    return render(request, 'campaign/create_character.html', {'form' : form, 'campaign' : campaign})


@login_required
def delete_campaign(request, campaign_id):
    """
    Allow User to Delete a Campaign
    """

    campaign = get_object_or_404(Campaign, id=campaign_id, user=request.user)


    # Once campaign has been deleted, User will be informed and redirected back to campaign list.
    if request.method == 'POST':
        campaign.delete()
        messages.success(request, f'{ campaign.name } has been deleted succesfully.')
        return redirect('campaign_list')
    
    return render(request, 'campaign/confirm_delete.html', {'campaign' : campaign})


@login_required
def delete_character(request, character_id):
    """
    Allow a user to delete a character from a campaign
    """
    character = get_object_or_404(Character, id=character_id, campaign__user=request.user)

    if request.method == 'POST':
        character.delete()
        return redirect('campaign_info', pk=character.campaign.id)
    
    return render(request, 'campaign/confirm_delete_character.html', {'character' : character})


@login_required
def update_character_stat(request, character_id, attribute, action):
    """
    Allow user to adjust characters stats in increments of +1 or -1
    """

    character = get_object_or_404(Character, id=character_id, campaign__user=request.user)

    valid_attributes = ['health', 'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']

    if attribute not in valid_attributes:
        return redirect('campaign info', pk=character.campaign.id)

    current_value = getattr(character, attribute)
    if action == 'increment' and current_value < 20:
        setattr(character, attribute, current_value + 1)
    elif action == 'decrement' and current_value > 1:
        setattr(character, attribute, current_value - 1)
    character.save()

    return redirect('campaign_info', pk=character.campaign.id)
