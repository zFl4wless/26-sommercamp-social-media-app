import datetime
import time

from django import template
from taggit.models import Tag

from blog.models import Post

register = template.Library()


@register.filter
def user_liked_post(post, user_id):
    return post.like_set.filter(author=user_id).exists()


@register.filter
def user_disliked_post(post, user_id):
    return post.dislike_set.filter(author=user_id).exists()


@register.filter
def get_comments(_, post):
    return post.comment_set.filter(post_id=post.id)


@register.filter
def formatted_join_date(_, profile):
    return profile.user.date_joined.strftime('%d.%m.%Y')


@register.filter
def get_tags(_, post):
    return Tag.objects.filter(post=post.id)
