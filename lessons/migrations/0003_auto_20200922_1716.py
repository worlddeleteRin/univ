# Generated by Django 3.0.8 on 2020-09-22 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itemtypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='itype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.Itemtypes'),
        ),
    ]