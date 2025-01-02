from django.db import models

# Create your models here.
class Monster(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    challenge_rating = models.IntegerField(default=0)
    health = models.IntegerField(default=0)
    armour = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name