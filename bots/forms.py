from django import forms
from .models import Bot

from django.utils import timezone


# All custom forms that will be displayed and used in the views.
class AddBotForm(forms.Form):
    """
    class Meta:
        model = Bot
        fields = ["bot_name", "description"]
    """
    bot_name = forms.CharField()
    description = forms.CharField()

    def addBot(self, user):
        bot = Bot(author=user, bot_name=self.data['bot_name'], add_date=timezone.now(), votes=0,
                  description=self.data['description'])
        bot.save()
        return bot


class UpdateBotForm(forms.ModelForm):
    class Meta:
        model = Bot
        fields = ["bot_name", "description"]
