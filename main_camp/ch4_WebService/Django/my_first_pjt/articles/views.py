from .models import Article
from .forms import ArticleForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST


# Create your views here.
def index(request):
    return render(request, "articles/index.html")


def articles(request):
    # Article에 저장된 걸 다 가져와 id 내림차순으로 정렬
    articles = Article.objects.all().order_by("-id")

    context = {
        "articles": articles,
    }

    return render(request, "articles/articles.html", context)


def article_detail(request, pk):
    # Article에 저장된 목록 중에 pk==pk인 글 가져오기
    # 없으면 404 error
    article = get_object_or_404(Article, pk=pk)

    context = {
        "article": article,
    }

    return render(request, "articles/article_detail.html", context)

@login_required
def create(request):
    # 기존 create 함수 부분
    if request.method == "POST":
        form = ArticleForm(request.POST)  # 데이터가 바인딩된(값이 채워진) Form
        if form.is_valid():  # Form이 유효하다면 데이터를 저장하고 다른 곳으로 redirect
            article = form.save()
            return redirect("articles:article_detail", article.pk)
    # 기존 new 함수 부분
    else:
        form = ArticleForm()

    context = {"form": form}
    return render(request, "articles/create.html", context)

@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect("articles:article_detail", article.pk)
    else:
        form = ArticleForm(instance=article)  # article의 값을 가지는 객체로 채워진 Form
    context = {
        "form": form,
        "article": article,
    }
    return render(request, "articles/update.html", context)

@require_POST
def delete(request, pk):
    if request.user.is_authenticated:  # 로그인이 된 상태여야만 삭제 가능 
        # Article에 저장된 목록 중에 pk==pk 인 글 가져오기
        article = get_object_or_404(Article, pk=pk)
        article.delete()
    return redirect("articles:articles")


def data_throw(request):
    return render(request, "articles/data-throw.html")


def data_catch(request):
    message = request.GET.get("message")
    context = {
        "message": message,
    }
    return render(request, "articles/data-catch.html", context)
