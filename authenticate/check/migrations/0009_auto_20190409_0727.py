# Generated by Django 2.2 on 2019-04-09 07:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0008_auto_20190409_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='checkOut',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 9, 7, 27, 20, 878795, tzinfo=utc), null=True),
        ),
    ]
