# Generated by Django 4.1.3 on 2022-11-30 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_myusercreate_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
            ],
        ),
    ]
