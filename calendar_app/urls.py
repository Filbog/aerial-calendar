from django.urls import path

from .views import EventListView, EventDetailView, calendar_view

urlpatterns = [
    path("list_layout/", EventListView.as_view(), name="list_layout"),
    path("", calendar_view, name="events"),
    path("<uuid:pk>/", EventDetailView.as_view(), name="event_detail"),
]
