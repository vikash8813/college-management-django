# Generated by Django 4.1.3 on 2022-11-21 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_course_seats'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='bgein',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='course',
            name='ends',
            field=models.DateField(default=None),
        ),
    ]
