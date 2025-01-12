# Generated by Django 5.1.4 on 2025-01-12 19:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0002_alter_character_charisma_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='health',
            field=models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2000)]),
        ),
    ]
