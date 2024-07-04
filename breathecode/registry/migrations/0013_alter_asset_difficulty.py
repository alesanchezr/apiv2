# Generated by Django 3.2.15 on 2022-10-05 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registry", "0012_auto_20221004_1943"),
    ]

    operations = [
        migrations.AlterField(
            model_name="asset",
            name="difficulty",
            field=models.CharField(
                blank=True,
                choices=[
                    ("HARD", "Hard"),
                    ("INTERMEDIATE", "Intermediate"),
                    ("EASY", "Easy"),
                    ("BEGINNER", "Beginner"),
                ],
                default=None,
                max_length=20,
                null=True,
            ),
        ),
    ]
