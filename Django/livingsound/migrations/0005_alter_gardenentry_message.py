# Generated by Django 4.2.2 on 2023-06-27 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livingsound', '0004_alter_gardenentry_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gardenentry',
            name='message',
            field=models.CharField(help_text='Enter the message', max_length=300),
        ),
    ]
