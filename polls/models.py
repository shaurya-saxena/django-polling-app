from django.db import models

from django.utils import timezone       #For custom function was_published_recently()
import datetime                         #For custom function was_published_recently()
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text 
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def is_this_privacy_invasion(self):
        return self.question_text == "Are you single?" or self.question_text == "How big is your twig?"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)  
    def __str__(self):
        return self.choice_text