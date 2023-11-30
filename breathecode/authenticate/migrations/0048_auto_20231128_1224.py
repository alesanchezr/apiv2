# Generated by Django 3.2.23 on 2023-11-28 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0047_auto_20231026_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinvite',
            name='asset_slug',
            field=models.SlugField(blank=True,
                                   help_text='If set, the user signed up because of an Asset',
                                   max_length=60,
                                   null=True),
        ),
        migrations.AlterField(
            model_name='userinvite',
            name='event_slug',
            field=models.SlugField(blank=True,
                                   help_text='If set, the user signed up because of an Event',
                                   max_length=120,
                                   null=True),
        ),
    ]
