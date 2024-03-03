from django.db import models

class groupData(models.Model):
    location = models.CharField(max_length=100)
    payment = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    orderLink = models.CharField(max_length=100)
    personCount = models.CharField(max_length=100)
    hostName = models.CharField(max_length=100)