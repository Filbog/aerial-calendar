from ..models import YearlyCalendar
from datetime import datetime
from .generate_calendar import generate_yearly_calendar


def get_or_create_calendar(year):
    # check if calendar already exists
    calendar_entry = YearlyCalendar.objects.filter(year=year).first()
    if calendar_entry:
        return calendar_entry.data

    # if not, create a new one
    calendar_data = generate_yearly_calendar(year)
    YearlyCalendar.objects.create(year=year, data=calendar_data)
    return calendar_data
