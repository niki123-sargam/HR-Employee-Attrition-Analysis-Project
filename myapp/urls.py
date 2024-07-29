from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('login/',views.login,name='login'),
    path('login/home/',views.home,name='login'),
    path('login/home/descriptive.html',views.descriptive,name='descriptive'),
    path('login/home/predictive.html',views.predictive,name='predictive'),
    path('login/home/getdata.html',views.getdata,name='getdata'),

]