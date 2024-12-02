from django.core.management.base import BaseCommand
from calendar_app.utils.generate_calendar import generate_yearly_calendar
from calendar_app.utils.get_or_create_calendar import get_or_create_calendar
from calendar_app.models import YearlyCalendar


class Command(BaseCommand):
    help = "Generates calendar data for the next X years (So far hard-coded) and saves to the database"

    def handle(self, *args, **kwargs):
        years_to_generate = [2025, 2026]

        for year in years_to_generate:
            if not YearlyCalendar.objects.filter(year=year).exists():
                get_or_create_calendar(year)

                self.stdout.write(
                    self.style.SUCCESS(f"Generated calendar data for {year}")
                )
            else:
                self.stdout.write(f"Calendar for {year} already exists")
