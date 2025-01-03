from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    View,
)
from .utils import generate_ics_file, serialize_events
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
    PermissionRequiredMixin,
)
from django.contrib.messages.views import SuccessMessageMixin
from .forms import EventForm
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.utils.translation import gettext as _


import json
from datetime import datetime

from .models import Event


def list_view(request):
    years = [datetime.now().year + i for i in range(2)]
    event_types = Event.TYPE_CHOICES
    events = Event.objects.filter(is_verified=True).order_by("start_date")
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
    events = Event.objects.all().filter(is_verified=True).order_by("created_at")
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
    success_message = "Event created"
    login_url = "account_login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.is_verified = self.request.user.groups.filter(
            name="verified"
        ).exists()
        response = super().form_valid(form)
        return response


class EventUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView
):
    model = Event
    form_class = EventForm
    template_name = "calendar/event_update.html"
    success_message = _("Event updated")
    success_url = reverse_lazy("events")
    login_url = "account_login"

    def test_func(self):
        event = self.get_object()
        return event.author == self.request.user


class EventDeleteView(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView
):
    model = Event
    success_message = _("Event deleted")
    success_url = reverse_lazy("events")
    login_url = "account_login"

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def test_func(self):
        event = self.get_object()
        return event.author == self.request.user


class UnverifiedEventsView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Event
    template_name = "calendar/unverified_events.html"
    context_object_name = "unverified_events"
    permission_required = "is_staff"
    raise_exception = True

    def get_queryset(self):

        return Event.objects.filter(is_verified=False)


@method_decorator(require_POST, name="dispatch")
class VerifyEventView(
    LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, View
):
    model = Event
    success_message = _("Event successfully verified")
    success_url = reverse_lazy("unverified_events")
    permission_required = "is_staff"
    raise_exception = True
    login_url = "account_login"

    def post(self, request, *args, **kwargs):
        print(kwargs)
        event = get_object_or_404(Event, id=kwargs.get("pk"))
        event.is_verified = True
        event.save()
        from django.contrib import messages

        messages.success(self.request, self.success_message)
        return redirect(self.success_url)


def download_event_ics_view(request, pk):
    event = get_object_or_404(Event, id=pk)
    return generate_ics_file.generate_ics_file(event)
