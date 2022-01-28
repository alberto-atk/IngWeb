# Generated by Django 4.0.1 on 2022-01-28 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_rename_login_client_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Nombre', max_length=15)),
                ('surname', models.CharField(help_text='Nombre', max_length=30)),
                ('mail', models.EmailField(help_text='Email address', max_length=30)),
                ('image', models.FilePathField()),
                ('description', models.CharField(help_text='Description', max_length=500)),
                ('title', models.CharField(help_text='Titles', max_length=500)),
                ('collaborations', models.CharField(help_text='Collaborations', max_length=500)),
            ],
        ),
    ]
