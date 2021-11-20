from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('store/',views.store,name='store'),
    path('store/<slug:slug>/',views.detail,name='detail')
]
