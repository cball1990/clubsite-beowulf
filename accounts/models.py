from django.db import models
from stdimage import StdImageField, JPEGField
from django.contrib.auth.models import User

class userImage(models.Model):
    profilePic = models.FileField(upload_to='images/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)