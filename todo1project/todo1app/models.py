from django.db import models


# Create your models here.
class Task(models.Model):
    # name = models.CharField(max_length=250)
    priority = models.IntegerField()
    task = models.CharField(max_length=250)
    date=models.DateField()



