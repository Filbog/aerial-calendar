from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
import uuid

User = get_user_model()


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False)

    description = models.TextField(blank=True, null=True)

    start_date = models.DateField()
    end_date = models.DateField()

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    organizer_alias = models.CharField(max_length=100)

    is_virtual = models.BooleanField(default=False)
    location = models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    TYPE_CHOICES = [
        ("competition", "Zawody"),
        ("workshop", "Warsztaty"),
        ("conference", "Konferencja"),
        ("show", "Show"),
        ("festival", "Festiwal"),
        ("convention", "Konwent"),
        ("other", "Inne"),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    is_aerial = models.BooleanField(default=True)

    main_link = models.URLField()
    additional_links = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("event_detail", args=[str(self.id)])
