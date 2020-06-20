# Generated by Django 2.2.5 on 2019-10-18 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handbook', '0003_handbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='handbook',
            name='group',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='handbook',
            name='is_link',
            field=models.BooleanField(default=False),
        ),
    ]
