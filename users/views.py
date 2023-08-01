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


def view_user(request, username:str):
    _create_profile_if_missing(User.objects.get(username=username))
    profile = Profile.objects.get(user__username=username)
    context = {
        "profile": profile
    }

    return render(request, 'users/profile_page.html', context=context)


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = 'users/profile_form.html'
    fields = ['bio']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        profile = self.get_object()
        print(self.request.user.id)
        print(profile.user.id)
        if self.request.user == profile.user:
            return True
        return False

    def get_success_url(self):
        return reverse("user-profile", args=[self.request.user.username])


def _create_profile_if_missing(user) -> None:
    if not (Profile.objects.filter(user=user).exists()):
        Profile.objects.create(user=user)
