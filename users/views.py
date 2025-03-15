from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()

def register_page(request):
    return render(request, 'users/register.html')

def index(request):
    return render(request, "layout.html")

class RegisterAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Lấy dữ liệu từ request
        data = request.data.copy()
        password1 = data.get('password1')
        password2 = data.get('password2')

        # Kiểm tra mật khẩu khớp
        if password1 != password2:
            return Response(
                {'error': 'Mật khẩu không khớp'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Đổi password1 thành password để serializer hiểu
        data['password'] = password1
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            try:
                phone = data.get('sdt', None)
                user = serializer.save()
                if phone:
                    user.phone = phone
                    user.save()
                return Response(
                    {'message': 'Đăng ký thành công', 'user': user.username},
                    status=status.HTTP_201_CREATED
                )
            except Exception as e:
                return Response(
                    {'error': f'Đã xảy ra lỗi khi tạo tài khoản: {str(e)}'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "Vui lòng nhập username và password"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "message": "Đăng nhập thành công",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email
                }
            }, status=status.HTTP_200_OK)
        return Response({"error": "Sai tài khoản hoặc mật khẩu"}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return redirect('/')