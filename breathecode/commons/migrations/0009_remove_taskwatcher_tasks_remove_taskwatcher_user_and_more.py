# Generated by Django 5.0.3 on 2024-03-06 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0008_merge_20240208_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskwatcher',
            name='tasks',
        ),
        migrations.RemoveField(
            model_name='taskwatcher',
            name='user',
        ),
        migrations.DeleteModel(name='TaskManager', ),
        migrations.DeleteModel(name='TaskWatcher', ),
    ]
