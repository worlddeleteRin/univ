# Generated by Django 3.0.8 on 2020-09-27 19:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0010_auto_20200927_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 27, 19, 4, 8, 770456, tzinfo=utc)),
        ),
    ]
