from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.cache import cache
from .models import Product
from .serializers import ProductSerializer


# Create your views here.
@api_view(["GET"])
def product_list(request):
    cache_key = "product_list"  # redis caching 사용 
    
    if not cache.get(cache_key):
        print("cache miss")
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        json_data = serializer.data
        cache.set(cache_key, json_data, 180)  # cache_key, cache_value, expired_time
    
    response_data = cache.get(cache_key)
    return Response(response_data)
