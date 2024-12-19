from django.urls import path
from . import views

app_name = "users"  # namespace 추가 

urlpatterns = [
    # users
    path("", views.users, name="users"),
    path("profile/<str:username>/", views.profile, name="profile"),
]
