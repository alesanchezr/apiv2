# Generated by Django 3.2.18 on 2023-05-12 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorship', '0022_auto_20230512_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendlywebhook',
            name='status_text',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='mentorprofile',
            name='calendly_uuid',
            field=models.CharField(blank=True,
                                   default=None,
                                   help_text='To be used by the calendly API',
                                   max_length=255,
                                   null=True),
        ),
        migrations.AlterField(
            model_name='mentorshipsession',
            name='calendly_uuid',
            field=models.CharField(blank=True,
                                   default=None,
                                   help_text='To be used by the calendly API',
                                   max_length=255,
                                   null=True),
        ),
    ]
