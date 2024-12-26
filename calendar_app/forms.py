from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "name",
            "description",
            "start_date",
            "end_date",
            "location",
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
            "description": "Opis",
            "start_date": "Data rozpoczęcia",
            "end_date": "Data zakończenia",
            "location": "Lokalizacja",
            "type": "Typ",
            "is_aerial": "Wydarzenie związane z akrobatyką powietrzną",
            "main_link": "Główny link - wydarzenie na FB, strona internetowa",
            "additional_url_1": "Dodatkowy link 1",
            "additional_label_1": "Dokąd prowadzi dodatkowy link 1",
            "additional_url_2": "Dodatkowy link 2",
            "additional_label_2": "Dokąd prowadzi dodatkowy link 2",
        }
        widgets = {
            "description": forms.Textarea(attrs={"rows": "5"}),
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
            "additional_label_1": forms.TextInput(
                attrs={"placeholder": "regulamin, katalog figur etc."}
            ),
            "additional_label_2": forms.TextInput(
                attrs={"placeholder": "regulamin, katalog figur etc."}
            ),
        }
