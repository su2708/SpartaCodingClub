from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [    
    path("", views.ArticleListAPIView.as_view(), name="article_list_create"),
    path("<int:pk>/", views.ArticleDetailAPIView.as_view(), name="article_detail"),
]
