from django import forms
from .models import Event
from django.utils.translation import gettext_lazy as _


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
            "name": _("Name of the event"),
            "description": _("Description"),
            "start_date": _("Start date"),
            "end_date": _("End date"),
            "location": _("Location"),
            "type": _("Type"),
            "is_aerial": _("Event related to aerials"),
            "main_link": _("Facebook event, event website"),
            "additional_url_1": _("Additional link 1"),
            "additional_label_1": _("Where does additonal link 1 lead to"),
            "additional_url_2": _("Additional link 2"),
            "additional_label_2": _("Where does additonal link 2 lead to"),
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
                attrs={"placeholder": _("Code of points, elements catalogue etc")}
            ),
            "additional_label_2": forms.TextInput(
                attrs={"placeholder": _("Code of points, elements catalogue etc")}
            ),
        }

        # labels = {
        #     "name": "Nazwa",
        #     "description": "Opis",
        #     "start_date": "Data rozpoczęcia",
        #     "end_date": "Data zakończenia",
        #     "location": "Lokalizacja",
        #     "type": "Typ",
        #     "is_aerial": "Wydarzenie związane z akrobatyką powietrzną",
        #     "main_link": "Główny link - wydarzenie na FB, strona internetowa",
        #     "additional_url_1": "Dodatkowy link 1",
        #     "additional_label_1": "Dokąd prowadzi dodatkowy link 1",
        #     "additional_url_2": "Dodatkowy link 2",
        #     "additional_label_2": "Dokąd prowadzi dodatkowy link 2",
        # }
        # widgets = {
        #     "description": forms.Textarea(attrs={"rows": "5"}),
        #     "start_date": forms.DateInput(
        #         attrs={"type": "date", "onfocus": "this.showPicker()"}
        #     ),
        #     "end_date": forms.DateInput(
        #         attrs={"type": "date", "onfocus": "this.showPicker()"}
        #     ),
        #     "type": forms.Select(),
        #     "main_link": forms.URLInput(attrs={"placeholder": "https://example.com"}),
        #     "additional_url_1": forms.URLInput(
        #         attrs={"placeholder": "https://example.com"}
        #     ),
        #     "additional_url_2": forms.URLInput(
        #         attrs={"placeholder": "https://example.com"}
        #     ),
        #     "additional_label_1": forms.TextInput(
        #         attrs={"placeholder": "regulamin, katalog figur etc."}
        #     ),
        #     "additional_label_2": forms.TextInput(
        #         attrs={"placeholder": "regulamin, katalog figur etc."}
        #     ),
        # }
