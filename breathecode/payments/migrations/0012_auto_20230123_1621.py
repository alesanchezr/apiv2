# Generated by Django 3.2.16 on 2023-01-23 16:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0011_auto_20230106_0029"),
    ]

    operations = [
        migrations.AlterField(
            model_name="consumptionsession",
            name="duration",
            field=models.DurationField(default=datetime.timedelta),
        ),
        migrations.AlterField(
            model_name="consumptionsession",
            name="request",
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
