# Generated by Django 5.0.2 on 2025-05-29 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='bathrooms',
            field=models.CharField(default='1'),
        ),
        migrations.AddField(
            model_name='property',
            name='bedrooms',
            field=models.CharField(default='1'),
        ),
        migrations.AddField(
            model_name='property',
            name='category',
            field=models.CharField(default='Apartment'),
        ),
        migrations.AddField(
            model_name='property',
            name='guests',
            field=models.CharField(default='1'),
        ),
    ]
