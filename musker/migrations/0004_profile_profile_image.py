# Generated by Django 5.0 on 2023-12-13 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musker', '0003_meep'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
