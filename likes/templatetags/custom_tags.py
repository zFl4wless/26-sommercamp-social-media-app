import datetime
import time

from django import template

register = template.Library()


@register.filter
def user_liked_post(post, user_id):
    return post.like_set.filter(author=user_id).exists()


@register.filter
def get_comments(_test, post):
    return post.comment_set.filter(post_id=post.id)


@register.filter
def formatted_join_date(test, profile):
    return profile.user.date_joined.strftime('%d.%m.%Y')
