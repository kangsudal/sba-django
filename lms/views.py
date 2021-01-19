from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def lmsIndex(req):
    return HttpResponse("This is lmsIndex view")
