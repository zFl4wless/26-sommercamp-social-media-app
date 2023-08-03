from django.urls import path

from followers import views

urlpatterns = [
    path('follow-user', views.follow_user, name='follow-user'),
]
