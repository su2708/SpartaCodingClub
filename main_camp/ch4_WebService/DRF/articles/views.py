from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import render
from .models import Article

# Create your views here.
def article_list_html(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "articles/article_list.html", context)

def json_01(request):
    articles = Article.objects.all()
    json_res = []

    for article in articles:
        json_res.append(
            {
                "title": article.title,
                "content": article.content,
                "created_at": article.created_at,
                "updated_at": article.updated_at,
            }
        )

    # return 해주는 값이 dict 형태면 safe=True, 나머진 False
    # 현재는 type(json_res) == list라서 safe=False
    return JsonResponse(json_res, safe=False)

def json_02(request):
    articles = Article.objects.all()
    res_data = serializers.serialize("json", articles)
    return HttpResponse(res_data, content_type="application/json")