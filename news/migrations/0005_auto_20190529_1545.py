# Generated by Django 2.1.7 on 2019-05-29 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20190529_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='author',
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]
