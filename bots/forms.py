from django import forms
from .models import Bot


# All custom forms that will be displayed and used in the views.
class AddBotForm(forms.ModelForm):
    class Meta:
        model = Bot
        fields = ["bot_name", "description"]


class UpdateBotForm(forms.ModelForm):
    class Meta:
        model = Bot
        fields = ["bot_name", "description"]
