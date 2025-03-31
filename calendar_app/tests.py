from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Event
from uuid import uuid4


class BaseEventTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", email="testuser@example.com", password="password"
        )
        self.other_user = get_user_model().objects.create_user(
            username="otheruser", email="otheruser@example.com", password="password"
        )

        self.event = Event.objects.create(
            name="Test Event",
            start_date="2025-01-01",
            end_date="2025-01-02",
            author=self.user,
            location="Test City",
            type="competition",
            main_link="http://example.com",
        )


class ListViewTests(BaseEventTestCase):
    def test_list_view_renders_correct_template(self):
        response = self.client.get(reverse("list_layout"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "calendar/list_layout.html")


class CalendarViewTests(BaseEventTestCase):
    def test_calendar_view_renders_correct_template(self):
        response = self.client.get(reverse("events"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "calendar/calendar_layout.html")


class EventDetailViewTests(BaseEventTestCase):
    def test_event_detail_view_requires_login(self):
        response = self.client.get(reverse("event_detail", args=[str(self.event.id)]))
        self.assertEqual(response.status_code, 302)

    def test_event_detail_view_authenticated_user(self):
        self.client.login(username="testuser", password="password")
        response = self.client.get(reverse("event_detail", args=[str(self.event.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "calendar/event_detail.html")


class EventCreateViewTests(BaseEventTestCase):
    def test_event_create_requires_login(self):
        response = self.client.get(reverse("event_create"))
        self.assertEqual(response.status_code, 302)

    def test_event_create_authenticated_user(self):
        self.client.login(username="testuser", password="password")
        response = self.client.get(reverse("event_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "calendar/event_create.html")


class EventUpdateViewTests(BaseEventTestCase):
    def test_event_edit_requires_login(self):
        response = self.client.get(reverse("event_edit", args=[str(self.event.id)]))
        self.assertEqual(response.status_code, 302)

    def test_event_edit_author_only(self):
        self.client.login(username="testuser", password="password")
        response = self.client.get(reverse("event_edit", args=[str(self.event.id)]))
        self.assertEqual(response.status_code, 200)

    def test_event_edit_forbidden_for_non_author(self):
        self.client.login(username="otheruser", password="password")
        response = self.client.get(reverse("event_edit", args=[str(self.event.id)]))
        self.assertEqual(response.status_code, 403)


class EventDeleteViewTests(BaseEventTestCase):
    def test_event_delete_requires_login(self):
        response = self.client.get(reverse("event_delete", args=[str(self.event.id)]))
        self.assertEqual(response.status_code, 302)

    def test_event_delete_author_only(self):
        self.client.login(username="testuser", password="password")
        response = self.client.post(reverse("event_delete", args=[str(self.event.id)]))
        self.assertEqual(response.status_code, 302)  # Success redirect
        self.assertFalse(Event.objects.filter(id=self.event.id).exists())

    def test_event_delete_forbidden_for_non_author(self):
        self.client.login(username="otheruser", password="password")
        response = self.client.get(reverse("event_delete", args=[str(self.event.id)]))
        self.assertEqual(response.status_code, 403)


class PermissionTestBase(TestCase):
    def setUp(self):
        self.staff_user = get_user_model().objects.create_superuser(
            username="staff_user",
            email="staff@example.com",
            password="password",
        )
        self.normal_user = get_user_model().objects.create_user(
            username="normal_user", email="normal@example.com", password="password"
        )
        self.verified_user = get_user_model().objects.create_user(
            username="verified_user", email="verified@example.com", password="password"
        )
        self.verified_user.groups.create(
            name="verified"
        )  # Add user to "verified" group
        self.unverified_event = Event.objects.create(
            id=uuid4(),
            name="Unverified Event",
            start_date="2025-01-01",
            end_date="2025-01-02",
            author=self.normal_user,
            location="City",
            type="competition",
            is_verified=False,
        )
        self.verified_event = Event.objects.create(
            id=uuid4(),
            name="Verified Event",
            start_date="2025-01-01",
            end_date="2025-01-02",
            author=self.verified_user,
            location="City",
            type="competition",
            is_verified=True,
        )


class UnverifiedEventsViewTests(PermissionTestBase):
    def test_access_unverified_events_as_staff(self):
        self.client.login(username="staff_user", password="password")
        response = self.client.get(reverse("unverified_events"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "calendar/unverified_events.html")
        self.assertContains(response, "Unverified Event")

    def test_access_unverified_events_as_non_staff(self):
        self.client.login(username="normal_user", password="password")
        response = self.client.get(reverse("unverified_events"))
        self.assertEqual(response.status_code, 403)  # Permission denied

    def test_access_unverified_events_as_anonymous(self):
        response = self.client.get(reverse("unverified_events"))
        self.assertEqual(response.status_code, 403)


class VerifyEventViewTests(PermissionTestBase):
    def test_verify_event_as_staff(self):
        self.client.login(username="staff_user", password="password")
        response = self.client.post(
            reverse("verify_event", args=[str(self.unverified_event.id)])
        )
        self.assertRedirects(response, reverse("unverified_events"))
        self.unverified_event.refresh_from_db()
        self.assertTrue(self.unverified_event.is_verified)

    def test_verify_event_as_non_staff(self):
        self.client.login(username="normal_user", password="password")
        response = self.client.post(
            reverse("verify_event", args=[str(self.unverified_event.id)])
        )
        self.assertEqual(response.status_code, 403)  # Permission denied
        self.unverified_event.refresh_from_db()
        self.assertFalse(self.unverified_event.is_verified)

    def test_verify_event_as_anonymous(self):
        response = self.client.post(
            reverse("verify_event", args=[str(self.unverified_event.id)])
        )
        self.assertEqual(response.status_code, 403)
        self.unverified_event.refresh_from_db()
        self.assertFalse(self.unverified_event.is_verified)
