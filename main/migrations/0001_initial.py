# Generated by Django 3.0.3 on 2020-04-07 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('like_count', models.IntegerField(default=0)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('describtion1', models.TextField(blank=True, default='', null=True)),
                ('describtion2', models.TextField(blank=True, default='', null=True)),
                ('job', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.IntegerField(blank=True, default=0, null=True)),
                ('birthday', models.CharField(blank=True, max_length=20, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('website', models.CharField(blank=True, max_length=200, null=True)),
                ('Email', models.EmailField(blank=True, default='', max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('like', models.IntegerField(default=0)),
                ('background_photo', models.ImageField(blank=True, null=True, upload_to='images')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/profile')),
                ('quick_info1', models.CharField(blank=True, max_length=40, null=True)),
                ('quick_info2', models.CharField(blank=True, max_length=40, null=True)),
                ('quick_info3', models.CharField(blank=True, max_length=40, null=True)),
                ('follow_count', models.IntegerField(default=0)),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('instagram', models.CharField(blank=True, max_length=100, null=True)),
                ('snapchat', models.CharField(blank=True, max_length=100, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='FollowSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followee', to='main.UserProfile')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target', to='main.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.UserProfile'),
        ),
    ]
