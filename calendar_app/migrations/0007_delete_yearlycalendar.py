# Generated by Django 5.1.2 on 2024-12-08 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("calendar_app", "0006_alter_event_type"),
    ]

    operations = [
        migrations.DeleteModel(
            name="YearlyCalendar",
        ),
    ]
