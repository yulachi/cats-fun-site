from django import forms

from .models import AlgoTask


class TaskForm(forms.ModelForm):
    class Meta:
        model = AlgoTask
        fields = ["a", "h", "r", "m"]

        labels = {
            "a": "Сторона куба",
            "h": "Высота цилиндра",
            "r": "Радиус основания цилиндра",
            "m": "Объем жидкости",
        }
