# Generated by Django 3.1.7 on 2021-04-20 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admissions", "0015_auto_20210302_0254"),
    ]

    operations = [
        migrations.AddField(
            model_name="cohort",
            name="private",
            field=models.BooleanField(default=False),
        ),
    ]
