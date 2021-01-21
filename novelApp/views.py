from django.shortcuts import render

# from django.http.response import HttpResponse

# Create your views here.
def post_list(req):
    return
def introPage(req,character1,character2):
    context = {"name1":character1,"name2":character2}
    return render(req,'introPage.html',context)