# Generated by Django 4.1.3 on 2022-11-18 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_event_email_event_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_image',
        ),
    ]