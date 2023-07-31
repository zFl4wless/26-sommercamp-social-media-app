from django import template

register = template.Library()


@register.filter
def user_liked_post(post, user_id):
    return post.like_set.filter(author=user_id).exists()
