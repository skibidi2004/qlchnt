from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import get_user_model

def register_page(request):
    return render(request, 'users/register.html')
def index(request):
    return render(request, "layout.html")

User = get_user_model()

class RegisterAPI(APIView):
    def post(self, request):
        email = request.data.get('email')
        sdt = request.data.get('sdt')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')

        if not email or not password1 or not password2:
            return Response({'error': 'Vui lòng nhập đầy đủ thông tin'}, status=status.HTTP_400_BAD_REQUEST)

        if password1 != password2:
            return Response({'error': 'Mật khẩu không khớp'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email đã tồn tại'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=email, email=email, password=password1)
        user.save()
        login(request, user)

        return Response({'message': 'Đăng ký thành công', 'user': user.username}, status=status.HTTP_201_CREATED)
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication

class LoginView(APIView):
    authentication_classes = [SessionAuthentication]  # Để đảm bảo API có thể nhận request
    permission_classes = [AllowAny]  # Cho phép tất cả mọi người truy cập API login

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "Vui lòng nhập username và password"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({"message": "Đăng nhập thành công"}, status=status.HTTP_200_OK)

        return Response({"error": "Sai tài khoản hoặc mật khẩu"}, status=status.HTTP_400_BAD_REQUEST)

 # Đăng xuất
class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return redirect('/')  # Chuyển về trang chủ