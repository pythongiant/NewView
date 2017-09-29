from django.db import models

# Create your models here.
class Reviews(models.Model):
    Title=models.CharField(max_length=100)
    Body=models.TextField()
    Tag=models.CharField(max_length=5000)
    author=models.CharField(max_length=5000)
    def __str__(self):
        return self.Title
class Subscription(models.Model):
    User=models.CharField(max_length=5000)
    Author=models.CharField(max_length=5000)
    alive= models.BooleanField(default=True)
    def __str__(self):
        return str(self.User) +" is subscribed to "+str(self.Author)