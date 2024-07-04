# Generated by Django 3.1.2 on 2020-10-29 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("admissions", "0011_auto_20201006_0058"),
        ("certificate", "0006_auto_20201005_2253"),
    ]

    operations = [
        migrations.CreateModel(
            name="CohortProxy",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("admissions.cohort",),
        ),
        migrations.AddField(
            model_name="specialty",
            name="certificate",
            field=models.OneToOneField(
                blank=True,
                default=None,
                help_text="This specialty represents only one certificate",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="admissions.certificate",
            ),
        ),
    ]
