# Generated by Django 4.2.3 on 2023-07-12 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_venue_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='ParkAppUser',
        ),
    ]
