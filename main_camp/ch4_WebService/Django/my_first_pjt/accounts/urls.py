from django.urls import path
from . import views

app_name = "accounts"  # namespace 추가

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
]
