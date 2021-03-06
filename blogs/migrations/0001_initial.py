# Generated by Django 3.2.7 on 2021-12-19 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(blank=True, max_length=100)),
                ('text', models.CharField(default='', max_length=900)),
                ('short_text', models.CharField(blank=True, max_length=100)),
                ('pub_date', models.DateTimeField(default='')),
                ('pub_author', models.CharField(default='', max_length=40)),
                ('image', models.ImageField(default='', upload_to='media')),
            ],
        ),
    ]
