# Generated by Django 2.2.5 on 2020-05-31 23:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0034_auto_20200531_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research',
            name='date_new',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 31, 23, 44, 27, 415315, tzinfo=utc), null=True),
        ),
    ]
