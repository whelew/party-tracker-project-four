from django.db import models
from django.core.validators import MinValueValidator


class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    character = models.ForeignKey(
        'campaign.Character',
        on_delete=models.CASCADE,
        related_name='inventories')

    def __str__(self):
        return f'Inventory for character: {self.character.name}'


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class InventoryItem(models.Model):
    id = models.AutoField(primary_key=True)
    inventory = models.ForeignKey(
        Inventory,
        on_delete=models.CASCADE,
        related_name='inventory_items')
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='inventory_items')
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)], default=1)

    class Meta:
        ordering = ['inventory', 'item']
        constraints = [
            models.UniqueConstraint(
                fields=['inventory', 'item'],
                name='unique_inventory_item')
        ]

    def __str__(self):
        return f'{self.quantity}x {self.item.name} in {self.inventory}'
