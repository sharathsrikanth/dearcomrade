# Generated by Django 3.1.7 on 2021-04-29 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_auto_20210429_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communitydetails',
            name='phnumber',
            field=models.CharField(max_length=11),
        ),
    ]
