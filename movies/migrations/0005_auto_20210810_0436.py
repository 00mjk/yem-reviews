# Generated by Django 3.1.4 on 2021-08-10 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20210809_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(default='default.jpg', upload_to='movie_posters'),
        ),
    ]
