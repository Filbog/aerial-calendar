from django.http import HttpResponse
from icalendar import Calendar, Event as ICalEvent
from datetime import date, timedelta


def generate_ics_file(event):
    cal = Calendar()
    cal.add("prodid", "-//Kalendarium Aerial//EN")
    cal.add("version", "2.0")

    # create an event
    ical_event = ICalEvent()
    ical_event.add("summary", event.name)
    ical_event.add("dtstart", event.start_date)
    # we have to add 1 to end_date since for whole day events, the start_date is inclusive while end_date is exclusive
    ical_event.add("dtend", event.end_date + timedelta(days=1))
    ical_event.add("location", event.location)

    description = [event.description or ""]
    description.append(f"Main link: {event.main_link}")
    if event.additional_url_1:
        label = event.additional_label_1 or "Additional link 1"
        description.append(f"{label}: {event.additional_url_1}")
    if event.additional_url_2:
        label = event.additional_label_2 or "Additional link 2"
        description.append(f"{label}: {event.additional_url_2}")

    ical_event.add("description", "\n".join(description))

    cal.add_component(ical_event)

    response = HttpResponse(
        cal.to_ical(),
        content_type="text/calendar",
    )
    response["Content-Disposition"] = f"attachment; filename={event.name}.ics"
    return response
