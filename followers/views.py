from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect

from followers.models import Follower


def follow_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        follower_id = request.POST.get('follower_id')

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return HttpResponse("Invalid user_id. User does not exist.")

        try:
            follower = User.objects.get(pk=follower_id)
        except User.DoesNotExist:
            return HttpResponse("Invalid post_id. Post does not exist.")

        user_followed = Follower.objects.filter(followed_user_id=user, follower_id=follower)
        if user_followed.exists():
            user_followed.delete()
            return redirect(request.META['HTTP_REFERER'])

        Follower.objects.create(followed_user=user, follower=follower)

        return redirect(request.META['HTTP_REFERER'])
