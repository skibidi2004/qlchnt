from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CategoryViewSet, ProductViewSet
from .views import CartViewSet, CartItemViewSet
from store.views import OrderViewSet

router = DefaultRouter()
router.register(r'store-users', UserViewSet, basename='store-user')
router.register(r'categories', CategoryViewSet, basename='cate')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'carts', CartViewSet, basename='cart')
router.register(r'cart-items', CartItemViewSet, basename='cartitem')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),

]
