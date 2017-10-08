from django.forms import forms,extras
from django import forms

GENRES=(
    ('Tech','Technology'),
    ('Movies','Movies'),
    ('Education','Education'),
    ('Art','Art'),
    ('Others','Other')
)


class Review(forms.Form):
    Title=forms.CharField(label="Give a Title",max_length=200,initial="add your title")
    Review=forms.CharField(label="Your Article",max_length=1000000000000000,initial="Type your article",widget=forms.Textarea)
    Tags=forms.CharField(label="add a tag. (Seperate with a ',') - eg. movie,event",max_length=5000,initial=" ")
    Genres=forms.ChoiceField(label="Choose a genre:",choices=GENRES)
class Authenticate(forms.Form):
    
    Username=forms.CharField(label="Username:",initial=" ")
    Password=forms.CharField(widget = forms.PasswordInput(),initial="") 

class Add(forms.Form):
    Username=forms.CharField(label="Username:",initial=" ")
    Password=forms.CharField(widget = forms.PasswordInput(),initial="")
    
    Email=forms.EmailField(label="Email Id:",initial="")
class Comment(forms.Form):
    Comment=forms.CharField(label="Type your comment")    
    