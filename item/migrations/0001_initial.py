# Generated by Django 5.1.4 on 2025-01-07 11:48

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('campaign', '0002_alter_character_charisma_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventories', to='campaign.character')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)])),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_items', to='item.inventory')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_items', to='item.item')),
            ],
            options={
                'ordering': ['inventory', 'item'],
                'constraints': [models.UniqueConstraint(fields=('inventory', 'item'), name='unique_inventory_item')],
            },
        ),
    ]
