from django.contrib import admin
from django.urls import path, include
from .views import post_list, post_detail,post_new, post_edit 

urlpatterns = [
    path('',post_list, name='post_list'),
    path('post/<int:pk>/',post_detail, name='post_detail'),
    path('post/new/',post_new, name='post_new'),
    path('post/<int:pk>/edit/',post_edit, name='post_edit'),    

]



"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

