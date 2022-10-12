# Generated by Django 4.1.2 on 2022-10-12 21:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DumUser',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='DumMsg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(default=datetime.datetime(2022, 10, 12, 21, 18, 33, 642102, tzinfo=datetime.timezone.utc), max_length=1500)),
                ('sent_msg', models.CharField(default=None, max_length=1500, null=True)),
                ('rec_msg', models.CharField(default=None, max_length=1500, null=True)),
                ('r_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.dumuser')),
            ],
        ),
    ]
