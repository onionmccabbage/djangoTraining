from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
# declare our data models here
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date      = models.DateTimeField('data published')
    # we can override the __str__ (for pretty output)
    def __str__(self):
        return self.question_text
    # we can add utility functions for our classes
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question    = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes       = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Weather(models.Model):
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    temperature = models.FloatField(default=22)
    def __str__(self):
        report_str = "{}: {} {}".format(self.city, self.description, self.temperature)
        return report_str