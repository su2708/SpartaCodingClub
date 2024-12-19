from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_POST, require_http_methods

@require_http_methods(["GET", "POST"])  # GET과 POST가 들어올 때만 login 실행 
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())  # 실제 로그인 처리를 진행하는 부분 
            next_path = request.GET.get("next") or "index"
            return redirect(next_path)
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)

@require_POST  # POST 요청이 들어올 때만 logout 함수 실행 
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)  # 실제 로그아웃 처리를 진행하는 부분 
    return redirect("articles:index")