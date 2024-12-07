# Generated by Django 5.1.2 on 2024-12-07 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("calendar_app", "0005_alter_event_location"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="type",
            field=models.CharField(
                choices=[
                    ("competition", "competition"),
                    ("workshop", "workshop"),
                    ("conference", "conference"),
                    ("show", "show"),
                    ("festival", "festival"),
                    ("convention", "convention"),
                    ("other", "other"),
                ],
                max_length=20,
            ),
        ),
    ]
