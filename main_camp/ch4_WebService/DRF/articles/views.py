from django.http import HttpResponse, JsonResponse
from django.core import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ArticleSerializer
from django.shortcuts import render, get_object_or_404
from .models import Article

class ArticleListAPIView(APIView):
    def get(self, request):
        # 1. article들을 다 가져오기 
        articles = Article.objects.all()
        # 2. 가져온 articles를 json으로 직렬화하는 serializer 선언 
        serializer = ArticleSerializer(articles, many=True)
        # 3. data를 직렬화해서 Response로 반환 
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        # raise_exception=True: serializer가 유효하지 않으면 에러 발생 
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class ArticleDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Article, pk=pk)

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        data = {"pk": f"{pk} is deleted."}
        return Response(data, status=status.HTTP_200_OK)