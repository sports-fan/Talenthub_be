# Generated by Django 2.2.7 on 2021-09-08 21:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_auto_20210831_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2021, 9, 8), verbose_name='Created Date of Notification'),
            preserve_default=False,
        ),
    ]
