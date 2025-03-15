from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def index(request):
    return render(request, "layout.html")

urlpatterns = [
    path("", index, name="index"),
    path("home/", index, name="home"),  # Thêm tuyến đường /home/
    path('admin/', admin.site.urls),
    path('api/', include('store.urls')),
    path("api/users/", include("users.urls")),
]