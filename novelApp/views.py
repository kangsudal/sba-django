from django.shortcuts import render

# from django.http.response import HttpResponse

# Create your views here.
def introPage(req,):
    return render(req,'introPage.html')