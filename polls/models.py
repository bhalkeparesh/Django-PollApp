
import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	publish_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

	def is_recent(self):
		return self.publish_date >= timezone.now()-datetime.timedelta(days=1)

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	percent = models.FloatField(default=0.0)

	def __str__(self):
		return self.choice_text