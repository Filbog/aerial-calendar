# Generated by Django 5.1.2 on 2024-12-07 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("calendar_app", "0003_remove_event_additional_links_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="is_virtual",
        ),
    ]
