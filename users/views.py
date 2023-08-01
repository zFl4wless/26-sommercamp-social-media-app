from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import UserRegisterForm
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def view_user(request, username):
    profile = Profile.objects.get(user_username=username)
    context = {
        "profile": profile
    }

    return render(request, "users/profile_page.html", context=context)
