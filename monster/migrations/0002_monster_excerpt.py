# Generated by Django 5.1.4 on 2025-01-05 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monster', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='monster',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
    ]