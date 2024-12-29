from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    ContactPageView,
    FAQPageView,
    YourAccountView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("faq/", FAQPageView.as_view(), name="faq"),
    path("your-account/", YourAccountView.as_view(), name="your_account"),
]
