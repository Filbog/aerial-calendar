from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .utils import generate_ics_file, serialize_events
from django.contrib.messages.views import SuccessMessageMixin
from .forms import EventForm
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
import json
from datetime import datetime

from .models import Event


# weird implementation of base template, and then partials depending on button click

# def render_to_response(self, context, **response_kwargs):
#     # Check if the request is made via HTMX
#     layout = self.request.GET.get("layout")
#     if layout == "list":
#         template = "calendar/list_layout.html"
#     elif layout == "calendar":
#         template = "calendar/calendar_layout.html"
#     else:
#         template = self.template_name

#     return HttpResponse(render_to_string(template, context))


def list_view(request):
    years = [datetime.now().year + i for i in range(2)]
    event_types = Event.TYPE_CHOICES
    events = Event.objects.all().order_by("start_date")
    events_serialized = serialize_events.serialize_events(events)

    return render(
        request,
        "calendar/list_layout.html",
        {"events": events_serialized, "event_types": event_types, "years": years},
    )


def calendar_view(request):
    years = [datetime.now().year + i for i in range(2)]
    print(years)
    event_types = Event.TYPE_CHOICES
    events = Event.objects.all().order_by("created_at")
    events_serialized = serialize_events.serialize_events(events)

    return render(
        request,
        "calendar/calendar_layout.html",
        {"events": events_serialized, "event_types": event_types, "years": years},
    )


class EventDetailView(DetailView):
    model = Event
    template_name = "calendar/event_detail.html"
    context_object_name = "event"


class EventCreateView(SuccessMessageMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = "calendar/event_create.html"
    success_url = reverse_lazy("events")
    success_message = "Wydarzenie utworzone"

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        return response


class EventUpdateView(SuccessMessageMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = "calendar/event_update.html"
    success_message = "Wydarzenie edytowane"
    success_url = reverse_lazy("events")


class EventDeleteView(SuccessMessageMixin, DeleteView):
    model = Event
    success_message = "Wydarzenie usunięte"
    success_url = reverse_lazy("events")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


def download_event_ics_view(request, pk):
    event = get_object_or_404(Event, id=pk)
    return generate_ics_file.generate_ics_file(event)
