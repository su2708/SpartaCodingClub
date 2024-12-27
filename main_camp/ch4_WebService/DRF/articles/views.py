from django.http import HttpResponse, JsonResponse
from django.core import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer
from django.shortcuts import render, get_object_or_404
from .models import Article

@api_view(["GET", "POST"])  # DRF의 method는 api_view라는 decorator가 필요 
def article_list(request):
    if request.method == "GET":
        # 1. article들을 다 가져오기 
        articles = Article.objects.all()
        # 2. 가져온 articles를 json으로 직렬화하는 serializer 선언 
        serializer = ArticleSerializer(articles, many=True)
        # 3. data를 직렬화해서 Response로 반환 
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        # raise_exception=True: serializer가 유효하지 않으면 에러 발생 
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        # partial=True: required인 fields들 중 일부만 수정할 수 있도록 변경 
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == "DELETE":
        article.delete()
        data = {"pk": f"{article.pk} is deleted."}
        return Response(data, status=status.HTTP_204_NO_CONTENT)