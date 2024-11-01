from django.test import TestCase, SimpleTestCase, override_settings
from django.urls import reverse, resolve
from unittest.mock import patch

from .views import HomePageView, AboutPageView


class HomePageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_resolves_homepageview(self):  # new
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class ErrorPagesTests(TestCase):
    def test_404(self):
        response = self.client.get("/non-existing-page/")
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")

    def test_405(self):
        response = self.client.post("/about/")
        self.assertEqual(response.status_code, 405)

    # for 401, we also need content that's restricted for only logged-in users

    # this one will make sense only after I have some restricted parts of the page
    # def test_403(self):
    #     response = self.client.get("/forbidden/")
    #     self.assertEqual(response.status_code, 403)
    #     self.assertTemplateUsed(response, "403.html")

    # @override_settings(DEBUG=False)
    # @patch("pages.views.HomePageView.get")
    # def test_500(self, mock_get):
    #     mock_get.side_effect = Exception("test 500")
    #     response = self.client.get("/", follow=False)

    #     self.assertEqual(response.status_code, 500)
    #     self.assertTemplateUsed(response, "errors/500.html")
    @override_settings(DEBUG=False)
    @patch("pages.views.HomePageView.get")
    def test_500(self, mock_view):
        self.client.raise_request_exception = False
        mock_view.side_effect = Exception()
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 500)
        self.assertTemplateUsed(response, "500.html")
