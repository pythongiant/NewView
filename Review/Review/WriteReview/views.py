#!usr/bin/python3

from django.shortcuts import render,redirect,get_object_or_404
from . import forms
from . import models
from django.contrib.auth.models import User #Import the User module
from django.contrib.auth import authenticate,login,logout#import some more stuff

#from .models import 
# Create your views here.
"""
username:srihari
password:pass1234
"""
recommendation=[]
def start(request):
    
    article=[i for i in models.Reviews.objects.all()]
    article.reverse()
    context={"article":article}
    return render(request,"WriteReview/index.html",context)
   
def RevDone(request):
    Rform=forms.Review

    if request.method == 'POST':
        form=Rform(request.POST)
        if form.is_valid():
            Title=form.cleaned_data['Title']
            Review=form.cleaned_data['Review']
            Tags=form.cleaned_data['Tags']
            models.Reviews.objects.create(Title=Title,Body=Review,Tag=Tags,author=request.user.username)
    return redirect("/")

def simscore(tag,test):
    score=0
    for i in tag:
        for y in test:
            if i == y:
                score+=1
                
    return (score)
def recommend(pk):
    global recommendation
    article=models.Reviews.objects.all()
    art_tags=[]
    art_tags_all=[]
   
    for i in article:
        art_tags.append(i.Tag)
    for i in art_tags:
        string=i.split(',')
        art_tags_all.append(string)

    recommend=0
    print(art_tags_all)
    
    for i in range(len(article)):
        tag=art_tags_all[i]
        sim=simscore(tag,art_tags_all[int(pk)-1])
        if sim>0:
            recommend=i+1
            recommendation.append(get_object_or_404(models.Reviews,pk=recommend))
    
    recommendation.reverse()



def ReviewDetail(request,rev_id):
    global recommendation
    print(rev_id)
    article=get_object_or_404(models.Reviews,pk=rev_id)
    print(article)
    recommend(rev_id)
    print(str(recommendation)+"  before")
    for i in recommendation:
        if i == article:
           recommendation.remove(i) 
            
    context={"article":article,"recommendations":recommendation}
    recommendation=[]

    return render(request,"WriteReview/MainPage.html",context)
    

def form(request):
    form = forms.Review()    
    context={"form":form}
    return render(request,"WriteReview/ArticleForm.html",context)
def signupForm(request):
    form=forms.Add()
    return render(request, 'WriteReview/add.html', {'signup': form})
def signup(request):
    if request.method == 'POST':
        form = forms.Add(request.POST)
        if form.is_valid():
            username = form.cleaned_data['Username']
            password = form.cleaned_data['Password']
            email=form.cleaned_data['Email']
            
            user = User.objects.create_user(username, email, password)
            user=authenticate(username=username,password=password)
            login(request,user)          
    return redirect("/")              
  
def loginForm(request):
    form=forms.Authenticate()
    return render(request, 'WriteReview/login.html', {'Login': form})      
    
def loginAction(request):
    if request.method == 'POST':
        form = forms.Authenticate(request.POST)
        if form.is_valid():
            username = form.cleaned_data['Username']
            password = form.cleaned_data['Password']
            user=authenticate(username=username,password=password)        
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                return render(request,"WriteReview/invalid.html",{})
def signout(request):
    logout(request)
    return redirect('/')            