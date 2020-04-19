from django.contrib import admin
from django.urls import path
from phani import views
from django.conf.urls import url,include

app_name = 'phani'

urlpatterns =[
    path('register/',views.register,name='register'),
    path('other/',views.other,name='other'),
    path('formpage/',views.form_name,name='formpage'),
    path('login/',views.user_login,name='user_login')
    ]