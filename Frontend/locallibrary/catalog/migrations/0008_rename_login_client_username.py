# Generated by Django 4.0.1 on 2022-01-28 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_remove_booking_enddate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='login',
            new_name='username',
        ),
    ]
