# Generated by Django 4.2.2 on 2023-06-23 18:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livingsound', '0002_remove_gardenentry_userentrynum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gardenentry',
            name='rating',
            field=models.IntegerField(help_text='Enter the rating of the quality of your plant (out of 5).\n| 1 - very poor (not doing well) | \n2 - poor | \n3 - no change | \n4 - good | \n5 - very good (doing very well)', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
