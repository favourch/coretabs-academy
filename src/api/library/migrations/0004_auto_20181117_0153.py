# Generated by Django 2.0.9 on 2018-11-16 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20181006_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='is_hidden',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='workshop',
            name='is_hidden',
            field=models.BooleanField(default=False),
        ),
    ]