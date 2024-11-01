from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site


class CustomUserTests(TestCase):

    def setUp(self):
        site = Site.objects.get_or_create(domain="localhost", name="localhost")[0]
        social_app = SocialApp.objects.create(
            provider="google", name="google", client_id="123", secret="1234567890"
        )
        social_app.sites.add(site)

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="will",
            email="will@email.com",
            password="testpass123",
        )
        self.assertEqual(user.username, "will")
        self.assertEqual(user.email, "will@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="superadmin",
            email="superadmin@email.com",
            password="testpass123",
        )
        self.assertEqual(admin_user.username, "superadmin")
        self.assertEqual(admin_user.email, "superadmin@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupPageTests(TestCase):
    username = "newuser"
    email = "newuser@email.com"

    def setUp(self):
        site = Site.objects.get_or_create(domain="example.com", name="example.com")[0]
        social_app = SocialApp.objects.create(
            provider="google", name="google", client_id="123", secret="1234567890"
        )
        social_app.sites.add(site)

        self.username = "newuser"
        self.email = "newuser@email.com"

    def test_signup_template(self):
        url = reverse("account_signup")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/signup.html")
        self.assertContains(response, "Sign Up")
        self.assertNotContains(response, "Hi there! I should not be on the page.")

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
