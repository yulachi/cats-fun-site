from django import forms

from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ("first_name", "last_name", "gender", "age")

        labels = {
            "first_name": "Имя",
            "last_name": "Фaмилия",
            "gender": "Пoл",
            "age": "Boзpacт",
        }
