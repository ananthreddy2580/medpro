
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index1',views.index1,name='index1'),
    path('display',views.display,name='display'),
    path('about/',views.about,name='about'),
    path('register',views.register,name='register'),
    path('registermore',views.registermore,name='registermore'),
    path('result',views.result,name='result'),
    path('search',views.search,name='search')
]
