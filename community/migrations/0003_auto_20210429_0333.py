# Generated by Django 3.1.7 on 2021-04-29 03:33

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_communityuserdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communitydetails',
            name='phnumber',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
