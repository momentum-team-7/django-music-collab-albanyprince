from django.db import models
from django.contrib.auth.models import AbstractUser

# built in Django user
# make decisions about users at the beginning, but everything else can change at any time.
class User(AbstractUser):
    pass

# class names are singular
class Artist(models.Model):
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=280)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=True, null=True, related_name='albums')
    # below True makes field optional
    release_year = models.IntegerField(blank = True, null=True)    
 #  ForeignKey relationship/ one-to-many relationship   
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='albums')    
# after model created, make migrations and migrate
    def __str__(self):
        return f"{self.title} | {self.artist} | {str(self.release_year)}"


