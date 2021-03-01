from django.db import models
from django.contrib.auth.models import AbstractUser

# built in Django user
# make decisions about users at the beginning, but everything else can change at any time.
class User(AbstractUser):
    pass

# class names are singular
class Album(models.Model):
    title = models.CharField(max_length=280)
    artist = models.CharField(max_length=280)
    # below True makes field optional
    release_year = models.IntegerField(blank = True, null=True)           
# after model created, make migrations and migrate
    def __str__(self):
        return self.title