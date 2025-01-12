from django.views.generic import TemplateView, ListView
from calendar_app.models import Event
from django.shortcuts import redirect
from django.urls import reverse


class AboutPageView(TemplateView):
    template_name = "about.html"


class ContactPageView(TemplateView):
    template_name = "contact.html"


class FAQPageView(TemplateView):
    template_name = "faq.html"
