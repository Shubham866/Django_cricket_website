# Generated by Django 3.2.7 on 2021-12-29 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0044_alter_ball_over'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ball',
            name='Over',
            field=models.DecimalField(decimal_places=1, max_digits=2, null=True),
        ),
    ]
