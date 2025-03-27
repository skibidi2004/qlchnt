from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

def index(request):
    return render(request, "layout.html")

urlpatterns = [
    path("", index, name="index"),
    path("home/", index, name="home"),  # Thêm tuyến đường /home/
    path('admin/', admin.site.urls),
    path('api/', include('store.urls')),
    path("api/users/", include("users.urls")),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)