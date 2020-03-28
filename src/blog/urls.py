from django.contrib import admin
from django.urls import path, include
from .views import (
    post_list,
    post_detail,
    post_new,
    post_edit,
    post_clap
)


app_name = 'blog'
urlpatterns = [
    path('',post_list, name='post_list'),
    path('post/<int:pk>/',post_detail, name='post_detail'),
    path('post/new/',post_new, name='post_new'),
    path('post/<int:pk>/edit/',post_edit, name='post_edit'),    
    path('post/<int:pk>/clap/',post_clap, name='post_clap'),    
]

