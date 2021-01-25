from django.db import models

class events(models.Model):
    title = models.CharField(max_length=30)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    description = models.TextField()
