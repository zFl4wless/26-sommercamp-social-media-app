from django.urls import path

from comment import views

urlpatterns = [
    path('send-comment', views.send_comment, name='send-comment'),
]
