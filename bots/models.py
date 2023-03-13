import datetime

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User


# All the models that allow to organize and structure the database.
class Bot(models.Model):
    """
    Model of a discord bot
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    bot_name = models.CharField(max_length=32)
    add_date = models.DateTimeField('date added', default=timezone.now)
    votes = models.IntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.bot_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.add_date <= now
