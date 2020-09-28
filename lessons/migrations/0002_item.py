# Generated by Django 3.0.8 on 2020-09-22 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('itype', models.CharField(default='', max_length=200)),
                ('itemurl', models.CharField(default='', max_length=2000)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.Subject')),
            ],
        ),
    ]
