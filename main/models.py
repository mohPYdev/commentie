from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User , on_delete= models.CASCADE , unique=True , related_name='user')
    describtion1 = models.TextField(default='',blank=True,null=True )
    describtion2 = models.TextField(default='' ,blank=True,null=True)
    job = models.CharField(max_length=100 ,blank=True,null=True)
    age = models.IntegerField(default=0 ,blank=True,null=True)
    birthday = models.CharField(max_length=20,blank=True,null=True)
    city = models.CharField(max_length=100,blank=True,null=True )
    website = models.CharField(max_length=200 ,blank=True,null=True)
    Email = models.EmailField(default='' ,blank=True,null=True)
    phone = models.CharField(max_length=15 ,blank=True,null=True)
    like = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    background_photo = models.ImageField(upload_to= 'images',default=' images / wall.JPG')
    picture = models.ImageField(upload_to='images/profile',default=' images / profile / defaultPic.JPG')
    quick_info1 = models.CharField(max_length=40 ,blank=True,null=True)
    quick_info2 = models.CharField(max_length=40,blank=True,null=True)
    quick_info3 = models.CharField(max_length=40,blank=True,null=True)
    follow_count = models.IntegerField(default=0)
    follower_count = models.IntegerField(default=0)
    facebook = models.CharField(max_length=100,blank=True,null=True)
    twitter = models.CharField(max_length=100,blank=True,null=True)
    instagram = models.CharField(max_length=100,blank=True,null=True)
    snapchat = models.CharField(max_length=100,blank=True,null=True)
    linkedin = models.CharField(max_length=100,blank=True,null=True)
    #follows = models.ManyToManyField("self" ,related_name='follows')

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    user = models.ForeignKey(UserProfile , on_delete= models.CASCADE)
    text = models.CharField(max_length=300)
    like_count = models.IntegerField(default=0)
    date = models.DateTimeField(default= timezone.now)


class Reply(models.Model):
    comment = models.ForeignKey(Comment , on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile , on_delete=models.CASCADE )
    text = models.CharField(max_length=200)
    date = models.DateTimeField( default= timezone.now)


class FollowSystem(models.Model):
    target = models.ForeignKey(UserProfile , on_delete= models.CASCADE,  related_name='target')
    followee = models.ForeignKey(UserProfile , on_delete= models.CASCADE , related_name= 'followee')

class Like(models.Model):
   comment = models.ForeignKey(Comment , on_delete=models.CASCADE , related_name='comment_like')
   user_like = models.ForeignKey(UserProfile , on_delete=models.CASCADE , related_name='user_like')




def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

