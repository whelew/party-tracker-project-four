from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Campaign(models.model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='campaigns')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self