from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Campaign, Character

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