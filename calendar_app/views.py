from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.messages.views import SuccessMessageMixin
from .forms import EventForm
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from django.urls import reverse_lazy
import json
from datetime import datetime

from .models import Event


class EventListView(ListView):
    model = Event
    template_name = "calendar/list_layout.html"
    context_object_name = "events"


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


def calendar_view(request):
    years = [datetime.now().year + i for i in range(2)]
    print(years)
    event_types = Event.TYPE_CHOICES
    events = Event.objects.all()
    events_serialized = json.dumps(
        [
            {
                "id": str(event.id),
                "name": event.name,
                "start_date": event.start_date.strftime("%d-%m-%Y"),
                "end_date": event.end_date.strftime("%d-%m-%Y"),
                "location": event.location,
                "type": event.type,
                "is_aerial": event.is_aerial,
                "main_link": event.main_link,
            }
            for event in events
        ]
    )
    print(events[0].start_date.isoformat())
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
