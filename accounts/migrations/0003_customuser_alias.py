# Generated by Django 5.1.2 on 2024-10-30 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_customuser_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="alias",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
