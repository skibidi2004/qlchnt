from django.urls import path
from .views import RegisterAPI, LoginView, LogoutView, register_page

urlpatterns = [
  
    path('users/register/', RegisterAPI.as_view(), name='api-register'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/logout/', LogoutView.as_view(), name='logout'),
    path('register-page/', register_page, name='register-page'), 
]
