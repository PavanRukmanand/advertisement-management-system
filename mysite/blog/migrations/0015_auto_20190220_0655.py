# Generated by Django 2.1.5 on 2019-02-20 06:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20190220_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 6, 55, 18, 744938, tzinfo=utc), verbose_name='date_joined'),
        ),
    ]