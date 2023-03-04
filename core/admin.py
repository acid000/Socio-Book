from django.contrib import admin

# Register your models here.
from .models import Profile
from .models import Profile, Post, LikePost, FollowersCount

# Register your models here.

admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowersCount)
admin.site.register(Profile)