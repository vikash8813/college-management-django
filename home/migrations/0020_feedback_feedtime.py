# Generated by Django 4.1.3 on 2022-12-01 04:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='feedtime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
