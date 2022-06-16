# Generated by Django 4.0.5 on 2022-06-15 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseprocess',
            name='state',
            field=models.CharField(choices=[(False, 'UnitedStates'), ('FR', 'France'), ('CN', 'China'), ('RU', 'Russia'), ('IT', 'Italy')], default=False, max_length=256, verbose_name='Состояние'),
        ),
    ]