# Generated by Django 4.0.1 on 2022-04-29 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welfare', '0015_rename_messages_message_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='message_admin',
            name='replay',
            field=models.CharField(default='', max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='message_admin',
            name='status',
            field=models.CharField(default='', max_length=240, null=True),
        ),
    ]
