from django.urls import path

from dislikes import views

urlpatterns = [
    path('dislike-post', views.dislike_post, name='dislike-post'),
]
