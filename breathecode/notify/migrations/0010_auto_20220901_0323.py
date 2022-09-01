# Generated by Django 3.2.15 on 2022-09-01 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notify', '0009_hook'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hook',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='hook',
            old_name='updated',
            new_name='updated_at',
        ),
        migrations.AddField(
            model_name='hook',
            name='last_call_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='hook',
            name='last_response_code',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='hook',
            name='sample_data',
            field=models.JSONField(blank=True,
                                   default=None,
                                   help_text='Use this as an example on what you will be receiving',
                                   null=True),
        ),
        migrations.AddField(
            model_name='hook',
            name='service_id',
            field=models.CharField(blank=True,
                                   default=None,
                                   max_length=64,
                                   null=True,
                                   verbose_name='Service ID'),
        ),
        migrations.AddField(
            model_name='hook',
            name='total_calls',
            field=models.IntegerField(default=0),
        ),
    ]