from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Campaign, Character
from .forms import CampaignForm

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
            campaign.save
            return redirect('campaign_list')
    else:
        form = CampaignForm()
    
    return render(request, 'campaign/create_campaign.html', {'form': form})