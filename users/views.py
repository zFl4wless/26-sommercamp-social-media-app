from django import forms
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import UpdateView

from .forms import UserRegisterForm
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            _create_profile_if_missing(user)
            messages.success(request, 'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def view_user(request, username: str):
    _create_profile_if_missing(User.objects.get(username=username))
    profile = Profile.objects.get(user__username=username)
    context = {
        "profile": profile
    }

    return render(request, 'users/profile_page.html', context=context)


def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile Updated")
            return redirect(f'/profile/{request.user.username}')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'users/profile_form.html', {'profile_form': profile_form, 'user_form': user_form})


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


def _create_profile_if_missing(user) -> None:
    if not (Profile.objects.filter(user=user).exists()):
        Profile.objects.create(user=user)

