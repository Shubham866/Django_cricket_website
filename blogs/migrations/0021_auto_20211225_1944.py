# Generated by Django 3.2.7 on 2021-12-25 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0020_auto_20211225_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='player_two_four',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requests_created9', to='blogs.player'),
        ),
        migrations.AlterField(
            model_name='match',
            name='player_two_three',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requests_created10', to='blogs.player'),
        ),
    ]
