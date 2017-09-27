#!usr/bin/python3

from django.shortcuts import render,redirect,get_object_or_404
from . import forms
from . import models

#from .models import 
# Create your views here.
"""
username:srihari
password:pass1234
"""
recommendation=[]
def start(request):
    form = forms.Review()    
    article=models.Reviews.objects.all()
    
    context={"form":form,"article":article}
    return render(request,"WriteReview/index.html",context)
   
def RevDone(request):
    Rform=forms.Review

    if request.method == 'POST':
        form=Rform(request.POST)
        if form.is_valid():
            Title=form.cleaned_data['Title']
            Review=form.cleaned_data['Review']
            Tags=form.cleaned_data['Tags']
            models.Reviews.objects.create(Title=Title,Body=Review,Tag=Tags)
    return redirect("/")

def simscore(tag,test):
    score=0
    for i in tag:
        for y in test:
            if i == y:
                score+=1
                
    return (score)
def recommend():
    global recommendation
    article=models.Reviews.objects.all()
    art_tags=[]
    art_tags_all=[]
    art_tags_all_refined=[]
    for i in article:
        art_tags.append(i.Tag)
    for i in art_tags:
        string=i.split(',')
        art_tags_all.append(string)
    """
    for i in art_tags_all:
        for y in i:
            art_tags_all_refined.append(y)
    """
    recommend=0
    print(art_tags_all)
    for i in range(len(article)):
        tag=art_tags_all[i]
        sim=simscore(tag,art_tags_all[0])
        if sim>0:
            recommend=i
            recommendation.append(recommend)
        



def ReviewDetail(request,rev_id):
    print(rev_id)
    article=get_object_or_404(models.Reviews,pk=rev_id)
    print(article)
    context={"article":article}
    recommend()
    print(recommendation)
    return render(request,"WriteReview/MainPage.html",context)
    

