# Generated by Django 3.0.8 on 2020-09-27 18:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0009_auto_20200927_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 27, 21, 42, 46, 215276)),
        ),
    ]