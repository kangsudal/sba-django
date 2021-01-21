from django.urls import path
from . import views

urlpatterns=[
    path('', views.post_list),
    path('<str:character1>/<str:character2>/',views.introPage),
]