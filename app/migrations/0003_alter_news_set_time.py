# Generated by Django 4.2.1 on 2024-06-13 17:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_news_set_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='set_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 13, 17, 59, 52, 71149, tzinfo=datetime.timezone.utc), verbose_name='Выбрать время'),
        ),
    ]
