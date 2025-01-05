from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Campaign(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='campaigns')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self
    

class Character(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    CLASS_TYPES = [
        ('barbarian', 'Barbarian'),
        ('bard', 'Bard'),
        ('cleric', 'Cleric'),
        ('druid', 'Druid'),
        ('fighter', 'Fighter'),
        ('monk', 'Monk'),
        ('paladin', 'Paladin'),
        ('ranger', 'Ranger'),
        ('rogue', 'Rogue'),
        ('sorcerer', 'Sorcerer'),
        ('warlock', 'Warlock'),
        ('wizard', 'Wizard'),
        ('artificer', 'Artificer'),
        ]

    character_class = models.CharField(max_length=50, choices=CLASS_TYPES)
    health = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)
    dexterity = models.IntegerField(default=0)
    constitution = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)
    charisma = models.IntegerField(default=0)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='characters')

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name