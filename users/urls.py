from django.contrib.auth import views as auth_views
from django.urls import path

import users.views as user_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', user_views.register, name='register'),
    path('profile/<str:username>', user_views.view_user, name='user-profile'),
    path('profile/', user_views.update_profile, name='profile-update')
]
