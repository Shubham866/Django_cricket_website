# Generated by Django 3.2.7 on 2022-01-01 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0053_auto_20211231_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='Date_match',
            field=models.DateField(),
        ),
    ]
