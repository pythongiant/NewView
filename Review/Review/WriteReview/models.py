from django.db import models

GENRES=(
    ('Tech','Technology'),
    ('Movies','Movies'),
    ('Education','Education'),
    ('Art','Art'),
    ('Others','Other')
)

# Create your models here.
class Reviews(models.Model):
    Title=models.CharField(max_length=100)
    Body=models.TextField()
    Tag=models.CharField(max_length=5000)
    author=models.CharField(max_length=5000)
    views=models.IntegerField()
    published=models.DateField()
    genre=models.CharField(choices=GENRES,max_length=20,default='Others')
    def __str__(self):
        return self.Title
class Subscription(models.Model):
    User=models.CharField(max_length=5000)
    Author=models.CharField(max_length=5000)
    alive= models.BooleanField(default=True)
    def __str__(self):
        return str(self.User) +" is subscribed to "+str(self.Author)
class Comment(models.Model):
    comment=models.CharField(max_length=10000)
    user=models.CharField(max_length=5000)
    article=models.CharField(max_length=100000000)
    def __str__(self):
        return str(self.comment)    
class Recommendation(models.Model):
    user=models.CharField(max_length=5000)
   
    article=models.CharField(max_length=500000)    
    def __str__(self):
        return str(self.user)+"-"+str(self.article)