from django.shortcuts import render

# Create your views here.
"""
username:srihari
password:pass1234
"""
def start(request):
    return render(request,"WriteReview/index.html",{})
