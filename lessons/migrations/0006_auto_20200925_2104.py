# Generated by Django 3.0.8 on 2020-09-25 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0005_auto_20200924_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='itemurl',
        ),
        migrations.AddField(
            model_name='item',
            name='imgurl',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='imgurl',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='imgurl',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
    ]
