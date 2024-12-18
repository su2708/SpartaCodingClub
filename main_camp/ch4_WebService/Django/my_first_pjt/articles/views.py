from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    return render(request, "index.html")

def articles(request):
    # Article에 저장된 걸 다 가져와 id 내림차순으로 정렬 
    articles = Article.objects.all().order_by("-id")
    
    context = {
        "articles": articles,
    }
    
    return render(request, "articles.html", context)

def article_detail(request, pk):
    # Article에 저장된 목록 중에 pk==pk 인 글 가져오기 
    article = Article.objects.get(pk=pk)
    
    context = {
        "article": article,
    }
    
    return render(request, "article_detail.html", context)

def new(request):
    return render(request, "new.html")

def create(request):
    # GET 방식으로 전달된 데이터를 받아서
    title = request.POST.get("title")
    content = request.POST.get("content")

    # 받은 데이터를 새로운 Article 모델을 이용해서 저장
    article = Article.objects.create(title=title, content=content)
    
    # 작업이 다 끝나면 articles.html로 redirect 
    return redirect('article_detail', article.pk)

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {"article": article} 
    return render(request, "edit.html", context)

def update(request, pk):
    title = request.POST.get("title")
    content = request.POST.get("content")
    
    article = Article.objects.get(pk=pk)
    article.title = title
    article.content = content
    article.save()
    
    return redirect("article_detail", article.pk)

def delete(request, pk):
    # method == "POST" 인 경우에만 article 삭제 
    if request.method == "POST":
        # Article에 저장된 목록 중에 pk==pk 인 글 가져오기 
        article = Article.objects.get(pk=pk)
        article.delete()
        return redirect("articles")
    return redirect("article_detail", pk)

def data_throw(request):
    return render(request, "data-throw.html")

def data_catch(request):
    message = request.GET.get("message")
    context = {
        "message": message,
    }
    return render(request, "data-catch.html", context)