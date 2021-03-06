# Generated by Django 3.2.7 on 2021-12-27 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0030_alter_ball_actual_run'),
    ]

    operations = [
        migrations.AddField(
            model_name='ball',
            name='Match',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogs.match'),
        ),
        migrations.CreateModel(
            name='player_match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Runs', models.IntegerField(default=0)),
                ('status', models.CharField(default='', max_length=100)),
                ('Balls_Faced', models.IntegerField(default=0)),
                ('four', models.IntegerField(default=0)),
                ('six', models.IntegerField(default=0)),
                ('runs_conceded', models.IntegerField(default=0)),
                ('wicket', models.IntegerField(default=0)),
                ('over', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('SR', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('Economy', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('Match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.match')),
            ],
        ),
    ]
