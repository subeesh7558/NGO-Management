# Generated by Django 4.0.1 on 2022-05-03 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welfare', '0020_remove_restaurant_registration_status_request_food'),
    ]

    operations = [
        migrations.AddField(
            model_name='request_food',
            name='reason',
            field=models.CharField(default='', max_length=240, null=True),
        ),
    ]