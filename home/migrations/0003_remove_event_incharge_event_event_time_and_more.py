# Generated by Django 4.1.3 on 2022-11-18 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='incharge',
        ),
        migrations.AddField(
            model_name='event',
            name='event_time',
            field=models.TimeField(default=None),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default=None, max_length=70),
        ),
        migrations.AddField(
            model_name='event',
            name='organiser',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
