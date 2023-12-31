# Generated by Django 4.2.1 on 2023-09-14 12:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debt',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2023, 9, 14, 12, 17, 17, 456489, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='savingsgoal',
            name='deadline',
            field=models.DateField(default=datetime.datetime(2023, 9, 14, 12, 17, 17, 489434, tzinfo=datetime.timezone.utc), help_text="When do you want to reach your saving's goal?"),
        ),
    ]
