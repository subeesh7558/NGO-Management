# Generated by Django 4.0.1 on 2022-05-05 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('welfare', '0026_message_admin_donuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message_admin',
            name='donuser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='welfare.user_registration'),
        ),
    ]