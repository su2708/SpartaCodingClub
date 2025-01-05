from django.urls import path
from .views import ChatView

app_name = "chatgpt"

urlpatterns = [
    path("newchat/", ChatView.as_view(), name="newchat")
]
