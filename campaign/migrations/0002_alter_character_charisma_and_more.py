# Generated by Django 5.1.4 on 2025-01-06 00:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='charisma',
            field=models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='character',
            name='constitution',
            field=models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='character',
            name='dexterity',
            field=models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='character',
            name='health',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='character',
            name='intelligence',
            field=models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='character',
            name='strength',
            field=models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='character',
            name='wisdom',
            field=models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)]),
        ),
    ]
