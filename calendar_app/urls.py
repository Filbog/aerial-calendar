from django.urls import path

from .views import EventListView, EventDetailView, calendar_view

urlpatterns = [
    # path("", EventListView.as_view(), name="events"),
    path("", calendar_view, name="events"),
    path("<uuid:pk>/", EventDetailView.as_view(), name="event_detail"),
]
