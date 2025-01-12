from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CampaignForm, CharacterForm
from item.models import Item, Inventory, InventoryItem
from .models import Campaign, Character
