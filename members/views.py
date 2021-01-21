from django.shortcuts import render, redirect
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

def stock(req):
    return HttpResponse("<h2>하경아 어서와 여기다가 주식 분석 페이지만들어줄게</h2>")

def git(req):
    return HttpResponse("<h2>git version</h2>")

def gu(req):
    num = req.GET.get('num','')
    return HttpResponse('<h1> gugu : '+num_gugu(int(num)) +'</h1>')

def num_gugu(num):
    ans='<br>'
    for i in range(10):
        ans+=f'{num} x {i} = {num*i} <br>' 
    return ans

def login(req):
    print(dir(req))
    if req.method== 'GET':
        return render(req, 'login.html')
    elif req.method == 'POST':
        username = req.POST.get('username', None)
        useremail = req.POST.get('useremail', None)

        err = {}

        if not (useremail and username) :
            err['err'] = '유효성이 잘못되었습니다.'
            return render(req, 'login.html', err)
        else:
            member = Members.objects.get(username=username)
            if useremail == member.useremail:#세션
                req.session['user'] = member.id
                return redirect('/members')

            return HttpResponse(f"<h1>{member.useremail}</h1>")

        # username = req.POST.get('username', None)
        # email = req.POST.get('password', None)

        # err = {}
        # if not(username and email) : 
        #     err['err'] ='비밀번호 오류'
        #     return  render(req, 'login.html', err)
        # else :
            ## db read
            ## session 만들기

        return redirect('/')

def login_after(req):
    user_id = req.session.get('user')
    if user_id:
        return HttpResponse(f'로그인 유저{user_id}')
    return redirect('/login')
    # return HttpResponse("세션읽기 & 세션 없으면 리다이렉트")

def logout(req):
    if req.session.get('user'):
        del(req.session['user'])
        return redirect('/')
        





'''
        if username == "exit" :
            return HttpResponse("<h2>나가기</h2>") #username == exit면 h2로 나가기를 출력
        elif username == "codingon":
            return render(req, 'login.html')
        return HttpResponse("<h2>"+username+"</h2>")
'''