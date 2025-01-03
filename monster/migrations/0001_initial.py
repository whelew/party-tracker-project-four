# Generated by Django 5.1.4 on 2025-01-03 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('challenge_rating', models.IntegerField(default=0)),
                ('health', models.IntegerField(default=0)),
                ('armour', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True)),
                ('type', models.CharField(choices=[('aberration', 'Aberration'), ('beast', 'Beast'), ('celestial', 'Celestial'), ('construct', 'Construct'), ('dragon', 'Dragon'), ('elemental', 'Elemental'), ('fey', 'Fey'), ('fiend', 'Fiend'), ('giant', 'Giant'), ('humanoid', 'Humanoid'), ('monstrosity', 'Monstrosity'), ('ooze', 'Ooze'), ('plant', 'Plant'), ('undead', 'Undead')], max_length=50)),
                ('size', models.CharField(choices=[('tiny', 'Tiny'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large'), ('huge', 'Huge'), ('gargantuan', 'Gargantuan')], max_length=50)),
            ],
        ),
    ]
