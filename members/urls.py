from django.urls import path
from . import views # 현재 프로제그에 view갖고온다
urlpatterns=[
        path('',views.index),
        path('git',views.git),
        path('test',views.test),
        path('signup', views.signup),
        path('onetk', views.onetk),
        path('stock', views.stock),
        path('gugu',views.gu),
        path('login',views.login)
]

