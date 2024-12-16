from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

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

def data_throw(request):
    return render(request, "data-throw.html")

def data_catch(request):
    message = request.GET.get("message")
    context = {
        "message": message,
    }
    return render(request, "data-catch.html", context)

