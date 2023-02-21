from django import forms
from .models import Bot


class AddBotForm(forms.ModelForm):
    class Meta:
        model = Bot
        fields = ["bot_name", "description"]


class UpdateBotForm(forms.ModelForm):
    class Meta:
        model = Bot
        fields = ["bot_name", "description"]
