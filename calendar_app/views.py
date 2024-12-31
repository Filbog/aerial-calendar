from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .utils import generate_ics_file, serialize_events
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import EventForm
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
import json
from datetime import datetime

from .models import Event


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


class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = "calendar/event_detail.html"
    context_object_name = "event"
    login_url = "account_login"


class EventCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = "calendar/event_create.html"
    success_url = reverse_lazy("events")
    success_message = "Wydarzenie utworzone"
    login_url = "account_login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        return response


class EventUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView
):
    model = Event
    form_class = EventForm
    template_name = "calendar/event_update.html"
    success_message = "Wydarzenie edytowane"
    success_url = reverse_lazy("events")
    login_url = "account_login"

    def test_func(self):
        event = self.get_object()
        return event.author == self.request.user


class EventDeleteView(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView
):
    model = Event
    success_message = "Wydarzenie usunięte"
    success_url = reverse_lazy("events")
    login_url = "account_login"

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def test_func(self):
        event = self.get_object()
        return event.author == self.request.user


def download_event_ics_view(request, pk):
    event = get_object_or_404(Event, id=pk)
    return generate_ics_file.generate_ics_file(event)
