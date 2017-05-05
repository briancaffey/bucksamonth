from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import UserProfile
from django.contrib.auth.models import User
from friends.models import Friend
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def add_or_remove_friends(request, username, verb):
    n_f = get_object_or_404(User, username=username)
    owner = request.user.userprofile
    new_friend = UserProfile.objects.get(user=n_f)

    if verb == "add":
        new_friend.followers.add(owner)
        Friend.make_friend(owner, new_friend)
    else:
        new_friend.followers.remove(owner)
        Friend.remove_friend(owner, new_friend)

    return redirect(new_friend.get_absolute_url())
