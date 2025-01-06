from django.views.generic import TemplateView, ListView
from calendar_app.models import Event
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse


def redirect_to_calendar(request):
    # Reverse the URL for the view in app2
    url = reverse("calendar_app:events")
    return redirect(url)


class AboutPageView(TemplateView):
    template_name = "about.html"


class ContactPageView(TemplateView):
    template_name = "contact.html"


class FAQPageView(TemplateView):
    template_name = "faq.html"


class YourAccountView(LoginRequiredMixin, ListView):
    template_name = "your_account.html"
    model = Event

    def get_queryset(self):
        return Event.objects.filter(author=self.request.user).order_by("-created_at")
