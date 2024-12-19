from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

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
    # Article에 저장된 목록 중에 pk==pk 인 글 가져오기 
    article = Article.objects.get(pk=pk)
    
    context = {
        "article": article,
    }
    
    return render(request, "articles/article_detail.html", context)

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

def update(request, pk):
    article = Article.objects.get(pk=pk)
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

def delete(request, pk):
    # method == "POST" 인 경우에만 article 삭제 
    if request.method == "POST":
        # Article에 저장된 목록 중에 pk==pk 인 글 가져오기 
        article = Article.objects.get(pk=pk)
        article.delete()
        return redirect("articles:articles")
    return redirect("articles:article_detail", pk)

def data_throw(request):
    return render(request, "articles/data-throw.html")

def data_catch(request):
    message = request.GET.get("message")
    context = {
        "message": message,
    }
    return render(request, "articles/data-catch.html", context)