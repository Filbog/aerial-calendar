from django.db import models
import json
from django.contrib.auth import get_user_model
from django.urls import reverse
import uuid
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False)

    description = models.TextField(blank=True, null=True)

    start_date = models.DateField()
    end_date = models.DateField()

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    organizer_alias = models.CharField(max_length=100)

    location = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    TYPE_CHOICES = [
        ("competition", _("competition")),
        ("workshop", _("workshop")),
        ("conference", _("conference")),
        ("show", _("show")),
        ("festival", _("festival")),
        ("convention", _("convention")),
        ("other", _("other")),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    is_aerial = models.BooleanField(default=True)

    is_verified = models.BooleanField(default=False)

    main_link = models.URLField(max_length=300)
    additional_url_1 = models.URLField(max_length=300, blank=True, null=True)
    additional_label_1 = models.CharField(max_length=100, blank=True, null=True)

    additional_url_2 = models.URLField(max_length=300, blank=True, null=True)
    additional_label_2 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("event_detail", args=[str(self.id)])

    def clean(self):
        # Ensure the end date is not earlier than the start date

        if self.end_date < self.start_date:
            raise ValidationError(_("Start date cannot be later than end date"))

    def save(self, *args, **kwargs):
        # Call clean() before saving to ensure validation

        self.clean()
        super().save(*args, **kwargs)
