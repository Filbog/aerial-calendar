from django.urls import path
from .views import (
    redirect_to_calendar,
    AboutPageView,
    ContactPageView,
    FAQPageView,
    YourAccountView,
)

urlpatterns = [
    # path("", redirect_to_calendar, name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("faq/", FAQPageView.as_view(), name="faq"),
    path("your-account/", YourAccountView.as_view(), name="your_account"),
]
