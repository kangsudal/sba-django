from django.urls import path
from . import views # 현재 프로제그에 view갖고온다
urlpatterns=[
        path('',views.index),
        path('git',views.git),
        path('test',views.test),
        path('signup', views.signup), #login.html
        path('onetk', views.onetk),   #a.html
        path('stock', views.stock),
        path('gugu',views.gu),
        path('login',views.login),    #login.html
        path('member',views.login_after),
]

