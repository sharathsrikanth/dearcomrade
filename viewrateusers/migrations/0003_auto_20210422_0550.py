# Generated by Django 3.1.7 on 2021-04-22 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewrateusers', '0002_auto_20210421_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userhistory',
            name='prevapartment1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userhistory',
            name='prevapartment2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userhistory',
            name='prevapartment3',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userpeertagging',
            name='userid1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userpeertagging',
            name='userid2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userpeertagging',
            name='userid3',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userpeertagging',
            name='userid4',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
