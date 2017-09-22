from django.db import models

# Create your models here.
class Reviews(models.Model):
    Title=models.CharField(max_length=100)
    Body=models.TextField()
    Tag=models.CharField(max_length=5000)
    def __str__(self):
        return self.Title
