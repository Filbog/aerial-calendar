from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.template.loader import render_to_string

from .models import Event


class EventListView(ListView):
    model = Event
    template_name = "calendar/events.html"
    context_object_name = "events"

    def render_to_response(self, context, **response_kwargs):
        # Check if the request is made via HTMX
        layout = self.request.GET.get("layout")
        if layout == "list":
            template = "calendar/list_layout.html"
        elif layout == "calendar":
            template = "calendar/calendar_layout.html"
        else:
            template = self.template_name

        return HttpResponse(render_to_string(template, context))


class EventDetailView(DetailView):
    model = Event
    template_name = "calendar/event_detail.html"
    context_object_name = "event"
