# Generated by Django 3.1.4 on 2021-08-09 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_user_is_organisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
