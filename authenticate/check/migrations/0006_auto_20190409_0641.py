# Generated by Django 2.2 on 2019-04-09 06:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0005_auto_20190409_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='checkOut',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime(2019, 4, 9, 6, 41, 11, 998652)),
        ),
    ]
