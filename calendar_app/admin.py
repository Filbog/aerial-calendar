from django.contrib import admin

# Register your models here.
from .models import Event, YearlyCalendar


@admin.register(YearlyCalendar)
class YearlyCalendarAdmin(admin.ModelAdmin):
    list_display = ("year", "created_at")


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass
