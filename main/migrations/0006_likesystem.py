# Generated by Django 3.0.5 on 2020-04-20 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_userprofile_follower_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_one', to='main.UserProfile')),
                ('likey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likey', to='main.UserProfile')),
            ],
        ),
    ]
