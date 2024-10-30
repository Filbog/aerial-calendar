from django.views.generic import ListView, DetailView

from .models import Event


class EventListView(ListView):
    model = Event
    template_name = "calendar/event_list.html"
    context_object_name = "events"


class EventDetailView(DetailView):
    model = Event
    template_name = "calendar/event_detail.html"
    context_object_name = "event"
