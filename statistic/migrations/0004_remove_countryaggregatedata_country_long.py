# Generated by Django 2.2.5 on 2020-05-29 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0003_countryhandbook_continent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countryaggregatedata',
            name='country_long',
        ),
    ]
