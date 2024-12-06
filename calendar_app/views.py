from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .forms import EventForm
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from django.urls import reverse_lazy
import json
from datetime import datetime

from .models import Event


# weird implementation of base template, and then partials depending on button click
class EventListView(ListView):
    model = Event
    template_name = "calendar/list_layout.html"
    context_object_name = "events"

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
    events = Event.objects.all()
    events_serialized = json.dumps(
        [
            {
                "id": str(event.id),
                "name": event.name,
                "start_date": event.start_date.isoformat(),
                "end_date": event.end_date.isoformat(),
                "is_virtual": event.is_virtual,
                "location": event.location if event.location else "",
                "type": event.type,
            }
            for event in events
        ]
    )
    return render(
        request,
        "calendar/calendar_layout.html",
        {"events": events_serialized, "years": years},
    )


class EventDetailView(DetailView):
    model = Event
    template_name = "calendar/event_detail.html"
    context_object_name = "event"


class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = "calendar/event_create.html"
    success_url = reverse_lazy("events")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
