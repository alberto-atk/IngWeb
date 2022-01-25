# Generated by Django 4.0.1 on 2022-01-25 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='catalog.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(default='', help_text='Username', max_length=20, primary_key=True, serialize=False),
        ),
    ]
