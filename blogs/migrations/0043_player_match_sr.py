# Generated by Django 3.2.7 on 2021-12-28 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0042_alter_player_match_economy'),
    ]

    operations = [
        migrations.AddField(
            model_name='player_match',
            name='SR',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
