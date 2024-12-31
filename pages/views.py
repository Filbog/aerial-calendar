from django.views.generic import TemplateView, ListView
from calendar_app.models import Event
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(TemplateView):
    template_name = "home.html"


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
