# Generated by Django 4.1.3 on 2022-11-30 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_rename_image_gallery_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='event_image',
            field=models.ImageField(upload_to='pics'),
        ),
    ]