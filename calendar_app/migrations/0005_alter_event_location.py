# Generated by Django 5.1.2 on 2024-12-07 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("calendar_app", "0004_remove_event_is_virtual"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="location",
            field=models.CharField(default="default_loc", max_length=100),
            preserve_default=False,
        ),
    ]
