"""
URL configuration for my_first_pjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

from articles import views

# url에 따라 어떤 View로 가야하는지 결정
urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/", views.index, name="index"),
    path("articles/", include("articles.urls")),  # articles의 urls.py에서 마저 처리
    path("users/", include("users.urls")),  # users의 urls.py에서 마저 처리
    path("accounts/", include("accounts.urls")),  # accounts의 urls.py에서 마저 처리
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)