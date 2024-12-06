from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "name",
            "start_date",
            "end_date",
            "location",
            "is_virtual",
            "type",
            "is_aerial",
            "main_link",
            "additional_url_1",
            "additional_label_1",
            "additional_url_2",
            "additional_label_2",
        ]
        labels = {
            "name": "Nazwa",
            "start_date": "Data rozpoczęcia",
            "end_date": "Data zakończenia",
            "location": "Lokalizacja",
            "is_virtual": "wydarzenie online",
            "type": "Typ",
            "is_aerial": "Wydarzenie związane z akrobatyką powietrzną",
            "main_link": "Główny link - wydarzenie na FB, strona internetowa",
        }
        widgets = {
            "start_date": forms.DateInput(
                attrs={"type": "date", "onfocus": "this.showPicker()"}
            ),
            "end_date": forms.DateInput(
                attrs={"type": "date", "onfocus": "this.showPicker()"}
            ),
            "type": forms.Select(),
            "main_link": forms.URLInput(attrs={"placeholder": "https://example.com"}),
            "additional_url_1": forms.URLInput(
                attrs={"placeholder": "https://example.com"}
            ),
            "additional_url_2": forms.URLInput(
                attrs={"placeholder": "https://example.com"}
            ),
        }
