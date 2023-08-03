import os

from django import template
from taggit.models import Tag

from followers.models import Follower

register = template.Library()


@register.filter
def user_liked_post(post, user_id):
    return post.like_set.filter(author=user_id).exists()


@register.filter
def user_disliked_post(post, user_id):
    return post.dislike_set.filter(author=user_id).exists()


@register.filter
def get_comments(_, post):
    return post.comment_set.filter(post_id=post.id).order_by('-date_posted')


@register.filter
def get_followers_count(_, profile):
    return Follower.objects.filter(followed_user_id=profile.user.id).count()


@register.filter
def get_followers(_, profile):
    follower_values = Follower.objects.filter(followed_user_id=profile.user.id).values_list('follower_id')

    def map_follower(follower):
        return follower[0]

    return list(map(map_follower, follower_values))


@register.filter
def formatted_join_date(_, profile):
    return profile.user.date_joined.strftime('%d.%m.%Y')


@register.filter
def get_tags(_, post):
    return Tag.objects.filter(post=post.id)


@register.filter
def check_file_type(_, url):
    name, extension = os.path.splitext(url.file.name)
    return extension
