from django.shortcuts import render
from .models import Campaign, Character

# Create your views here.
def campaign_list(request):
    """
    Display an individual :model:`campaign.Campaign`.

    **Context**

    ``monster``
        An instance of :model:`campaign.Campaign`.

    **Template:**

    :template:`campaign/campaign.html`
    """
     
    current_campaign = Campaign.objects.all()

    return render(
        request, "campaign/campaign.html",
        {"current_campaign": current_campaign},
        )