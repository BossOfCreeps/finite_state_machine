# Generated by Django 4.0.5 on 2022-06-15 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256, verbose_name='Текст')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessA',
            fields=[
                ('baseprocess_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.baseprocess')),
            ],
            bases=('main.baseprocess',),
        ),
        migrations.CreateModel(
            name='ProcessB',
            fields=[
                ('baseprocess_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.baseprocess')),
            ],
            bases=('main.baseprocess',),
        ),
    ]