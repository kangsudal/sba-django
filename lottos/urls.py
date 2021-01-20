from django.urls import path
from . import views # 현재 프로제그에 view갖고온다
urlpatterns=[
        path('',views.index),
]

