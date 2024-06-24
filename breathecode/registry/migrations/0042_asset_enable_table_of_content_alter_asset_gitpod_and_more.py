# Generated by Django 5.0.3 on 2024-05-28 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0041_asset_is_auto_subscribed'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='enable_table_of_content',
            field=models.BooleanField(default=True,
                                      help_text='If true, it shows a tabled on contents on top of the lesson'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='gitpod',
            field=models.BooleanField(
                default=False,
                help_text='If true, it means it can be opened on cloud provisioning vendors like Gitpod or Codespaces'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='interactive',
            field=models.BooleanField(db_index=True, default=False, help_text='If true, it means is learnpack enabled'),
        ),
    ]
