from django.urls import path

from likes import views

urlpatterns = [
    path('like-post', views.like_post, name='like-post'),
]
