# Generated by Django 4.0.1 on 2022-01-28 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_rename_dateend_booking_enddate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='endDate',
        ),
    ]
