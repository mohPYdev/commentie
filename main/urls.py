from django.urls import path
from . import  views

app_name = 'main'

urlpatterns = [
    path('profile/<int:pk>' , views.UserProfileDetailView.as_view() , name = 'profile'),
    path('profile/edit/<int:pk>' , views.UserProfileUpdateView.as_view(), name = 'edit_profile'),
    path('profile/edit/photo/<int:pk>', views.UserPhotoUpdateView.as_view(), name='change_picture'),
    path('like/<int:pk>' , views.addLike , name = 'add_like'),
    path('follow/<int:pk>/<int:pkprof>' , views.addFollow , name = 'add_follow'),
    path('reply/<int:pk>/<int:commentpk>' , views.ReplyCreateView.as_view() , name='create_reply'),
    path('comment/<int:pk>' , views.CommentCreateView.as_view() , name = 'create_comment'),
    path('delete/follow/<int:pk>' , views.FollowDeleteView.as_view() , name = 'delete_follow'),
]

