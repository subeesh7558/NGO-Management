# Generated by Django 4.0.1 on 2022-05-04 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welfare', '0021_request_food_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='request_food',
            name='time',
            field=models.DateField(blank=True, null=True),
        ),
    ]