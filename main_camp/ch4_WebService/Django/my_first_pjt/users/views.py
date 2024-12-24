from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


# Create your views here.
def users(request):
    return render(request, "users/users.html")


def profile(request, username):
    member = get_object_or_404(get_user_model(), username=username)
    context = {
        "member": member,
    }
    return render(request, "users/profile.html", context)

@require_POST
def follow(request, user_pk):
    # request.user == "현재 로그인한 사람"
	# member == "누군가의 프로필"
    if request.user_is_authenticated:
        member = get_object_or_404(get_user_model(), pk=user_pk)
        if request.user != member:  # 자기 자신을 팔로우하는 경우 제외 
            if request.user in member.followers.all():
                member.followers.remove(request.user)
            else:
                member.followers.add(request.user)
        return redirect("users:profile", member.username)
    return redirect("accounts:login")
        