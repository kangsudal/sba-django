from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Members


def index(request):
    return HttpResponse("<h1>hi kangsudal</h1>")

def test(request):
    return HttpResponse("<h1>이곳은 members앱의 test views입니다</h1>")

#home으로 보냄 redirect('/')
def signup(req):
    if req.method == 'POST' :
        username = req.POST['username']  
        email = req.POST['email'] 
        member = Members(
            username = username,
            useremail = email
        )   
        member.save()
        res_data = {}
        res_data['res']="등록성공"#등록성공여부
        return render(req, 'index.html',res_data)

    return render(req, 'index.html')

def onetk(req):
    return render(req,'a.html')


def git(req):
    return HttpResponse("<h2>git version</h2>")





'''
        if username == "exit" :
            return HttpResponse("<h2>나가기</h2>") #username == exit면 h2로 나가기를 출력
        elif username == "codingon":
            return render(req, 'login.html')
        return HttpResponse("<h2>"+username+"</h2>")
'''