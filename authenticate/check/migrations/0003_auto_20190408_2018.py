# Generated by Django 2.2 on 2019-04-08 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0002_auto_20190408_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='checkOut',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
