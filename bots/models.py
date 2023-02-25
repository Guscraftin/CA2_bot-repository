import datetime

from django.db import models
from django.utils import timezone


# All the models that allow to organize and structure the database.
class Author(models.Model):
    author_name = models.CharField(max_length=200)
    join_date = models.DateTimeField('date joined')

    def __str__(self):
        return self.author_name

    def was_join_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.join_date <= now


class Bot(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
    bot_name = models.CharField(max_length=32)
    add_date = models.DateTimeField('date added', default=timezone.now)
    votes = models.IntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.bot_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.add_date <= now
