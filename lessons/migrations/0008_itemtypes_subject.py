# Generated by Django 3.0.8 on 2020-09-26 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0007_auto_20200925_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemtypes',
            name='subject',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='lessons.Subject'),
            preserve_default=False,
        ),
    ]
