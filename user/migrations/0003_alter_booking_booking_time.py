# Generated by Django 3.2 on 2021-07-16 14:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
