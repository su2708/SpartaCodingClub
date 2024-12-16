from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello, name="hello"),
    # data
    path("data-throw/", views.data_throw, name="data-throw"),
    path("data-catch/", views.data_catch, name="data-catch"),
]