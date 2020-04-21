from django.shortcuts import render , redirect , get_object_or_404 ,reverse
import random
from .models import UserProfile , Reply , Comment , FollowSystem , Like
from django.views.generic import (
        UpdateView,
        DeleteView,
        ListView,
        CreateView,
        DetailView,
        RedirectView,
)
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
# Create your views here.





class UserProfileUpdateView(LoginRequiredMixin,UpdateView):
    model = UserProfile

    template_name = 'main/edit_profile.html'

    fields = (
        'describtion1',
        'describtion2',
        'job',
        'age',
        'birthday',
        'city',
        'website',
        'Email',
        'phone',
        'quick_info1',
        'quick_info2',
        'quick_info3',
        'facebook',
        'twitter',
        'instagram',
        'snapchat',
        'linkedin',
    )


    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.request.user.user == self.object:
            return redirect('/profile/1')
        else:
            return super(UserProfileUpdateView, self).get(request, *args, **kwargs)

    def get_success_url(self):
        return '/profile/'+ str(self.request.user.user.pk)



class UserPhotoUpdateView(LoginRequiredMixin,UpdateView):
    model = UserProfile

    template_name = 'main/change_photo.html'

    fields = (
        'background_photo',
        'picture',
    )


    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.request.user.user == self.object:
            return redirect('/profile/1')
        else:
            return super(UserPhotoUpdateView, self).get(request, *args, **kwargs)

    def get_success_url(self):
        return '/profile/'+ str(self.request.user.user.pk)




class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'main/index.html'


    def get_success_url(self):
        return '/profile/'+ str(self.request.user.user.pk) + '#comment'

    def get_context_data(self, **kwargs):
        context = super(UserProfileDetailView , self).get_context_data( **kwargs)
        context['object'] = UserProfile.objects.get(pk = self.kwargs['pk'])
        if context['object'].comment_count > 0:
            random_comment = context['object'].comment_set.get(pk = random.randint(1 , context['object'].comment_count))
            context['random_comment'] = context['object'].comment_set.get(pk= 1)
                #random_comment.text
            context['comments'] = context['object'].comment_set.all()
        listfollow = []
        for follow in self.request.user.user.target.all():
            listfollow.append(follow.followee)
        context['following'] = listfollow

        listlike = []
        for like in self.request.user.user.user_like.all():
            listlike.append(like.comment)
        context['liked_comments'] = listlike

        if context['object'] != self.request.user.user and context['object'] in context['following']:
            context['unfollow'] = FollowSystem.objects.get(target = self.request.user.user , followee = context['object'])
        return context



def addLike(request , pk):
    comment = Comment.objects.get(pk = pk)

    if comment.comment_like.filter(user_like = request.user.user):
        return redirect('/profile/' + str(comment.user.pk) + '#comment')
    else:
        user_like = get_object_or_404(UserProfile , pk = request.user.user.pk)
        like = Like.objects.create(comment = comment , user_like = user_like)
        comment.like_count += 1
        comment.user.like += 1
        comment.save()
        comment.user.save()
        like.save()
        return redirect('/profile/'+ str(comment.user.pk)+'#comment')


def addFollow(request , pk , pkprof):
    user = UserProfile.objects.get(pk =pk)
    profuser = UserProfile.objects.get(pk = pkprof)
    user.follow_count += 1
    profuser.follower_count += 1
    follow = FollowSystem.objects.create(target = user , followee = profuser)
    user.save()
    profuser.save()
    follow.save()
    return redirect('/profile/' + str(pk))


class FollowDeleteView(DeleteView):
    model = FollowSystem

    def get_success_url(self):
        return '/profile/'+ str(self.request.user.user.pk)
    
    def post(self, request, *args, **kwargs):
        
        self.request.user.user.follow_count -= 1
        follow = FollowSystem.objects.get(pk = self.kwargs['pk'])
        prof = follow.followee
        prof.follower_count -= 1
        self.request.user.user.save()
        prof.save()
        return super(FollowDeleteView, self).post(request , *args , **kwargs)

class ReplyCreateView(CreateView):
    model = Reply

    fields = (
        'text',
    )

    template_name = 'main/replyCreate.html'

    def get_context_data(self, **kwargs):
        context = super(ReplyCreateView , self).get_context_data(**kwargs)
        comment = Comment.objects.get(pk = self.kwargs['commentpk'])
        context['comment'] = comment
        context['object'] = UserProfile.objects.get(pk = self.kwargs['pk'])
        return context

    def get_success_url(self):
        return '/profile/'+ str(self.kwargs['pk'])+'#reply'

    def form_valid(self, form):
        user = get_object_or_404(UserProfile, id = self.request.user.user.pk)
        comment = get_object_or_404(Comment , id = self.kwargs['commentpk'])
        form.instance.user = user
        form.instance.comment = comment
        return super(ReplyCreateView, self).form_valid(form)


class CommentCreateView(CreateView):
    template_name = 'main/commentCreate.html'
    model = Comment
    fields = (
        'text',
    )

    def get_success_url(self):
        return '/profile/' + str(self.kwargs['pk']) + '#comment'

    def get_context_data(self, **kwargs):
        context = super(CommentCreateView ,self).get_context_data(**kwargs)
        context['object'] = UserProfile.objects.get(pk = self.kwargs['pk'])
        context['comments'] = context['object'].comment_set.all()
        return context

    def form_valid(self, form):
            user = get_object_or_404(UserProfile, id = self.request.user.user.pk)
            form.instance.user = user
            return super(CommentCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):

        self.request.user.user.comment_count += 1
        self.request.user.user.save()
        return super(CommentCreateView, self).post(request, *args, **kwargs)

