# Generated by Django 4.0.1 on 2022-01-28 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_rename_workers_worker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='image',
            field=models.CharField(max_length=100),
        ),
    ]
