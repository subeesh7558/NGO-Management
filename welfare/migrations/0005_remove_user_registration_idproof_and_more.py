# Generated by Django 4.0.1 on 2022-04-26 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('welfare', '0004_delete_login_delete_signup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_registration',
            name='idproof',
        ),
        migrations.RemoveField(
            model_name='user_registration',
            name='photo',
        ),
    ]
