from django.contrib import admin
from .models import UserProfile , Comment , Reply , FollowSystem
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(FollowSystem)
