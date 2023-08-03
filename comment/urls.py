from django.urls import path

from comment import views

urlpatterns = [
    path('send-comment', views.send_comment, name='send-comment'),
    path('delete-comment', views.delete_comment, name='delete-comment'),
    path('edit-comment', views.edit_comment, name='edit-comment')
]
