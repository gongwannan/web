# Generated by Django 2.1.7 on 2019-05-29 07:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luntan', '0005_auto_20190529_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiezi',
            name='mostrecently',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 29, 15, 37, 20, 352896)),
        ),
    ]
