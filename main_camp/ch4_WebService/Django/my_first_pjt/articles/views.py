from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def users(request):
    return render(request, "users.html")

def hello(request):
    name = "Yun"
    tags = ["#joyful", "#bright", "#cute"]
    books = {
        "today": "토지",
        "yesterday": "태백산맥",
        "tomorrow": "우정",
    }
    
    context = {
        "name": name,
        "tags": tags,
        "books": books,
    }
    
    return render(request, "hello.html", context)