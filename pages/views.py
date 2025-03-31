from django.views.generic import TemplateView


class AboutPageView(TemplateView):
    template_name = "about.html"


class ContactPageView(TemplateView):
    template_name = "contact.html"


class FAQPageView(TemplateView):
    template_name = "faq.html"
