from django.urls import path
from . import views

app_name = "articles"  # namespace 추가

urlpatterns = [
    path("", views.articles, name="articles"),
    path("create/", views.create, name="create"),  # 새로운 article 생성
    path("<int:pk>/", views.article_detail, name="article_detail"),  # article 상세
    path("<int:pk>/delete/", views.delete, name="delete"),  # article 삭제
    path("<int:pk>/update/", views.update, name="update"),  # article 수정
    #
    path("index/", views.index, name="index"),
    # data
    path("data-throw/", views.data_throw, name="data-throw"),
    path("data-catch/", views.data_catch, name="data-catch"),
]
