#!usr/bin/python3
import datetime
from django.shortcuts import render,redirect,get_object_or_404
from . import forms
from . import models
from django.contrib.auth.models import User #Import the User module
from django.contrib.auth import authenticate,login,logout#import some more stuff
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
import os
#from .models import 
# Create your views here.


recommendation=[]
prev_recommendations=[]
prev_recommendationsb=[]
def tops():
    pass



def tags(pk,tag):
    obj=get_object_or_404(models.Reviews,pk=pk)
    tags=obj.Tag
    art_tags=tags
    art_tags_all=[]
    string=art_tags.split(',')
    for i in string:
        if i == tag:
            return True
    

def start(request):
    
    article=[i for i in models.Reviews.objects.all()][-9:]
    article.reverse()
    prev_recommendation=list(set(prev_recommendations))
    print(prev_recommendation)
    for i in prev_recommendation:
        models.Recommendation.objects.create(user=request.user.username,article=i)
        for y in models.Recommendation.objects.all():
            if models.Recommendation.objects.filter(article=i).count() >1:
                y.delete()           
    #for movie articles                
    movie=[]
    for i in models.Reviews.objects.all():
        key = i.pk
        if tags(key,"movie")==True or tags(key,"movies") == True or i.genre == "Movies":
            
            print(key)
            movie.append(i)
    print(movie)            

    prev_recommendatioa=models.Recommendation.objects.all().filter(user=request.user.username)        
    prev_recommendationsb.append(str(prev_recommendatioa))
    print("STUFF:"+str(prev_recommendations))
    context={"article":article,"previous":prev_recommendatioa,"movie":movie,"Prev_len":len(prev_recommendations)}
    return render(request,"WriteReview/index.html",context)
   
def RevDone(request):
    Rform=forms.Review

    if request.method == 'POST':
        form=Rform(request.POST)
        if form.is_valid():
            Title=form.cleaned_data['Title']
            Review=form.cleaned_data['Review']
            Tags=form.cleaned_data['Tags']
            genre=form.cleaned_data['Genres']
            models.Reviews.objects.create(Title=Title,Body=Review,Ta=Tags,author=request.user.username,views=0,published=datetime.datetime.now())
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
            prev_recommendations.append(get_object_or_404(models.Reviews,pk=recommend))
    recommendation.reverse()
    prev_recommendations.reverse()


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

    form=forms.Comment()            
    article.views+=1  
      
    article.save()
    if request.method == 'POST':
        form = forms.Comment(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['Comment']
            user=request.user.username
            models.Comment.objects.create(comment=comment,user=user,article=article.Title)
    all_comments=models.Comment.objects.all().filter(article=article.Title)          
    if len(recommendation)==0:
        recommendation.append("No recommendations")
    
    context={"article":article,"recommendations":recommendation,"form":form,"comments":all_comments}
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
    form=forms.Add()
    if request.method == 'POST':
        form = forms.Add(request.POST)
        if form.is_valid():
            username = form.cleaned_data['Username']
            password = form.cleaned_data['Password']
            email=form.cleaned_data['Email']
            try:
                user = User.objects.create_user(username, email, password)
                user=authenticate(username=username,password=password)
                login(request,user)          
                return redirect("/")              
            except IntegrityError:
                
                error="Try another Username"
                return render(request,"WriteReview/add.html",{"error":error,"form":form})        
    
  
def loginForm(request):
    form=forms.Authenticate()
    return render(request, 'WriteReview/login.html', {'Login': form})      
    
def loginAction(request):
    form=forms.Authenticate()
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
                error="Wrong Username or Password"
                return render(request,"WriteReview/index.html",{"Login":form,"error":error})

def signout(request):
    logout(request)
    return redirect('/')         

def authour(request,name):
    ArticleObject=models.Reviews.objects.all()
    articles=[]
    for article in ArticleObject:
        author_name=article.author
        if author_name == name:
            articles.append(article)
    context={"article":articles,"name":name}
    return render(request,"WriteReview/author.html",context)
def subs(request,name):
    print ("author name")
    print(name )
    models.Subscription.objects.create(User=request.user.username,Author=name,alive=True)
    return redirect("/")

def subscriptions(request):
    name=request.user.username
    all_model=models.Subscription.objects.all().filter(User=name)
    arts=[]
    for i in all_model:
        authour=i.Author
        all_articles=models.Reviews.objects.all()
        for article in all_articles:
            author_for_article=article.author
            if author_for_article==authour:
               arts.append(article)     
    context={"article":arts}        
    return render(request,"WriteReview/subscription.html",context)           
