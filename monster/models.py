from django.db import models


class Monster(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    challenge_rating = models.IntegerField(default=0)
    health = models.IntegerField(default=0)
    armour = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    excerpt = models.TextField(blank=True)

    MONSTER_TYPES = [
        ('aberration', 'Aberration'),
        ('beast', 'Beast'),
        ('celestial', 'Celestial'),
        ('construct', 'Construct'),
        ('dragon', 'Dragon'),
        ('elemental', 'Elemental'),
        ('fey', 'Fey'),
        ('fiend', 'Fiend'),
        ('giant', 'Giant'),
        ('humanoid', 'Humanoid'),
        ('monstrosity', 'Monstrosity'),
        ('ooze', 'Ooze'),
        ('plant', 'Plant'),
        ('undead', 'Undead'),
    ]

    MONSTER_SIZES = [
        ('tiny', 'Tiny'),
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
        ('huge', 'Huge'),
        ('gargantuan', 'Gargantuan'),
    ]

    type = models.CharField(max_length=50, choices=MONSTER_TYPES)
    size = models.CharField(max_length=50, choices=MONSTER_SIZES)

    class Meta:
        ordering = ['challenge_rating', 'name']

    def __str__(self):
        return f"Monster:{self.name} Challenge Rating:{self.challenge_rating}"
