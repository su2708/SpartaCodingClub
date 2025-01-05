from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .chatbot import chatbot

# Create your views here.
class ChatView(APIView):
    def post(self, request):
        user_msg = request.data.get("user_msg")
        chat_msg = chatbot(user_msg).content
        return Response({"chat_msg": chat_msg})