# Generated by Django 4.0.1 on 2022-04-28 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('welfare', '0014_messages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='messages',
            new_name='message_admin',
        ),
    ]
