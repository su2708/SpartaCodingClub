from .models import Article, Comment
from .forms import ArticleForm, CommentForm
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
    comment_form = CommentForm()  # 댓글 폼 
    comments = article.comments.all().order_by("-pk")  # 최신 순으로 댓글 보여주기 
    context = {
        "article": article,
        "comment_form": comment_form,
        "comments": comments,
    }

    return render(request, "articles/article_detail.html", context)

@login_required
def create(request):
    # 기존 create 함수 부분
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)  # 데이터가 바인딩된(값이 채워진) Form
        if form.is_valid():  # Form이 유효하다면 데이터를 저장하고 다른 곳으로 redirect
            article = form.save(commit=False)
            article.author = request.user
            article.save()
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
    if article.author == request.user:  # 작성자만 수정 가능 
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
    else:
        return redirect("articles:articles")

@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user.is_authenticated:  # 로그인이 된 상태여야만 삭제 가능 
        if article.author == request.user:  # 작성자만 글 삭제 가능 
            # Article에 저장된 목록 중에 pk==pk 인 글 가져오기
            article = get_object_or_404(Article, pk=pk)
            article.delete()
    return redirect("articles:articles")

@require_POST
def comment_create(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)  # instance를 생성하지만 바로 DB에 저장되지 않도록 commit=False 
        comment.article = article
        comment.user = request.user  # 댓글 작성자 추가 
        comment.save()
    return redirect("articles:article_detail", article.pk)

@require_POST
def comment_delete(request, pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if comment.user == request.user:
            comment.delete()
    return redirect("articles:article_detail", pk)

def data_throw(request):
    return render(request, "articles/data-throw.html")

def data_catch(request):
    data = request.GET.get("message")
    context = {
        "data": data,
    }
    return render(request, "articles/data-catch.html", context)
