# Generated by Django 3.1.4 on 2021-08-06 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20210727_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_organisor',
            field=models.BooleanField(default=False),
        ),
    ]
