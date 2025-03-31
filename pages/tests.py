from django.test import TestCase, override_settings
from django.urls import reverse
from unittest.mock import patch

from .views import AboutPageView


class ErrorPagesTests(TestCase):
    def test_404(self):
        response = self.client.get("/non-existing-page/")
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")

    def test_405(self):
        response = self.client.post("/about/")
        self.assertEqual(response.status_code, 405)

    @override_settings(DEBUG=False)
    @patch("pages.views.AboutPageView.get")
    def test_500(self, mock_view):
        self.client.raise_request_exception = False
        mock_view.side_effect = Exception()
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 500)
        self.assertTemplateUsed(response, "500.html")
