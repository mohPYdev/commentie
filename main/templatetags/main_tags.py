from django import template
register = template.Library()


from ..models import UserProfile , Like , Comment , FollowSystem


@register.simple_tag
def liked_one(user , comment):
    return user.user_like.filter(comment=comment)

@register.simple_tag
def follow_reply(user , reply_user):
    return user.target.filter(followee = reply_user)

@register.simple_tag
def follow_one(user , obj):
    return user.target.filter(followee = obj)

@register.simple_tag
def unfollow_one(user , obj):
    if follow_one(user , obj):
        return FollowSystem.objects.get(target= user , followee = obj)
    else:
        return None