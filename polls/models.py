from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=100)
    public_data = models.DateTimeField()
    votes = models.BigIntegerField()

