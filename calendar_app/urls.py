from django.urls import path

from .views import (
    EventListView,
    EventDetailView,
    calendar_view,
    EventCreateView,
    EventUpdateView,
    EventDeleteView,
)

urlpatterns = [
    path("list_layout/", EventListView.as_view(), name="list_layout"),
    path("", calendar_view, name="events"),
    path("<uuid:pk>/", EventDetailView.as_view(), name="event_detail"),
    path("event_create/", EventCreateView.as_view(), name="event_create"),
    path("<uuid:pk>/edit/", EventUpdateView.as_view(), name="event_edit"),
    path("<uuid:pk>/delete/", EventDeleteView.as_view(), name="event_delete"),
]
