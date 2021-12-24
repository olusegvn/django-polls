import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question = models.CharField(max_length=200, unique=True)
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    @admin.display(
        boolean=True,
        ordering='publish_date',
        description='Was published recently'
    )
    def was_published_recenetly(self):
        now = timezone.now()
        was_published_recently = now-datetime.timedelta(days=1) <= self.publish_date <= now
        return was_published_recently


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice
