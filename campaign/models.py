from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from item.models import Inventory


class Campaign(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='campaigns')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


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

    SET_STAT = [MinValueValidator(1), MaxValueValidator(20)]

    character_class = models.CharField(max_length=50, choices=CLASS_TYPES)
    health = models.IntegerField(
        default=10, validators=[MinValueValidator(1), MaxValueValidator(2000)])
    strength = models.IntegerField(default=10, validators=SET_STAT)
    dexterity = models.IntegerField(default=10, validators=SET_STAT)
    constitution = models.IntegerField(default=10, validators=SET_STAT)
    intelligence = models.IntegerField(default=10, validators=SET_STAT)
    wisdom = models.IntegerField(default=10, validators=SET_STAT)
    charisma = models.IntegerField(default=10, validators=SET_STAT)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE,
                                 related_name='characters')

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        """
        Creates inventory when character is saved.
        """
        super().save(*args, **kwargs)
        Inventory.objects.get_or_create(character=self)

    def __str__(self):
        return self.name
