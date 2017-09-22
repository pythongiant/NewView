from django.forms import forms,extras
from django import forms


class Review(forms.Form):
    Title=forms.CharField(label="Give a Title",max_length=200,initial="add your title")
    Review=forms.CharField(label="Your Review",max_length=100000,initial="Type your Review",widget=forms.Textarea)
    Tags=forms.CharField(label="add a tag. (Seperate with a ',') - eg. movie,event",max_length=5000,initial=" ")
