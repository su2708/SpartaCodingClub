from django.urls import path
from . import views

urlpatterns = [
    path("", views.articles, name="articles"),
    path("new/", views.new, name="new"),  # 새로운 article 작성 
    path("create/", views.create, name="create"),  # 새로운 article 생성
    path("<int:pk>/", views.article_detail, name="article_detail"),  # article 상세 
    path("<int:pk>/delete/", views.delete, name="delete"),  # article 삭제 
    path("<int:pk>/edit/", views.edit, name="edit"),  # article 수정 사항 작성 
    path("<int:pk>/update/", views.update, name="update"),  # article 수정 사항 반영 
    #
    path("index/", views.index, name="index"),
    # data
    path("data-throw/", views.data_throw, name="data-throw"),
    path("data-catch/", views.data_catch, name="data-catch"),
]