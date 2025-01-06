from django.urls import path

from .views import (
    EventDetailView,
    list_view,
    calendar_view,
    EventCreateView,
    EventUpdateView,
    EventDeleteView,
    UnverifiedEventsView,
    VerifyEventView,
    download_event_ics_view,
)


urlpatterns = [
    path("list_layout/", list_view, name="list_layout"),
    path("", calendar_view, name="events"),
    path("<uuid:pk>/", EventDetailView.as_view(), name="event_detail"),
    path("event_create/", EventCreateView.as_view(), name="event_create"),
    path("<uuid:pk>/edit/", EventUpdateView.as_view(), name="event_edit"),
    path("<uuid:pk>/delete/", EventDeleteView.as_view(), name="event_delete"),
    path("<uuid:pk>/download-ics/", download_event_ics_view, name="download_event_ics"),
    path(
        "unverified-events/", UnverifiedEventsView.as_view(), name="unverified_events"
    ),
    path("verify-event/<uuid:pk>/", VerifyEventView.as_view(), name="verify_event"),
]
