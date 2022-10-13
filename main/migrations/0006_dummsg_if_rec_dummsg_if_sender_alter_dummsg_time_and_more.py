# Generated by Django 4.1.2 on 2022-10-13 11:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_dummsg_sender_alter_dummsg_time_alter_failedmsg_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='dummsg',
            name='if_rec',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dummsg',
            name='if_sender',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='dummsg',
            name='time',
            field=models.TimeField(default=datetime.datetime(2022, 10, 13, 11, 54, 12, 938801, tzinfo=datetime.timezone.utc), max_length=1500),
        ),
        migrations.AlterField(
            model_name='failedmsg',
            name='time',
            field=models.TimeField(default=datetime.datetime(2022, 10, 13, 11, 54, 12, 941811, tzinfo=datetime.timezone.utc), max_length=1500),
        ),
    ]
