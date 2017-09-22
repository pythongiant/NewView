#!usr/bin/python3

from django.shortcuts import render
from . import forms
#from .models import 
# Create your views here.
"""
username:srihari
password:pass1234
"""

def start(request):
    form = forms.Review()    
    context={"form":form}
    return render(request,"WriteReview/index.html",context)
def RevDone(request):
    Rform=forms.Review

    if request.method == 'POST':
        form=Rform(request.POST)
        if form.is_valid():
            Title=form.cleaned_data['Title']
            Review=form.cleaned_data['Review']
            Tags=form.cleaned_data['Tags']
            print(Title)
    return render(request,"WriteReview/index.html",{})