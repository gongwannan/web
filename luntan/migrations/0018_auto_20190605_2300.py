# Generated by Django 2.1.7 on 2019-06-05 15:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20190605_2300'),
        ('luntan', '0017_auto_20190603_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shoucang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': '帖子收藏关系',
                'verbose_name': '帖子收藏关系',
            },
        ),
        migrations.AlterField(
            model_name='tiezi',
            name='mostrecently',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 5, 23, 0, 29, 384649)),
        ),
        migrations.AddField(
            model_name='shoucang',
            name='tiezi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guanzhushu', to='luntan.Tiezi'),
        ),
        migrations.AddField(
            model_name='shoucang',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoucang', to='login.User'),
        ),
    ]