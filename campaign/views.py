from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
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

    return render(request, 'campaign/campaign_info.html', {'campaign': campaign})    

@login_required
def create_character(request, campaign_id):
    """
    Allow user to add characters to campaign based on campaign id.
    """
    campaign = get_object_or_404(request, id=campaign_id, user=request.user)

    if request.method == 'POST':
        form = CharacterForm(request.POST, user=request.user)
        if form.is_valid():
            character = form.save(commit=False)
            character.campaign = campaign # link the character to campaign/id
            character.save()
            return redirect('campaign_info', pk=campaign_id) 
    else:
        form = CharacterForm(user=request.user)
    
    return render(request, 'campaign/create_character.html', {'form' : form, 'campaign' : campaign})