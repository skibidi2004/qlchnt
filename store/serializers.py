from rest_framework import serializers
from .models import User, Category, Product, Cart, CartItem
from store.models import Product
from store.models import Order 
from store.models import OrderItem, CartItem, ProductImage

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # Hiển thị thông tin danh mục
    images = ProductImageSerializer(many=True, read_only=True)  # Lấy danh sách ảnh

    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'description', 'price', 'stock', 'discount', 'created_at', 'updated_at', 'images']

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source="product.name")

    class Meta:
        model = CartItem
        fields = ["id", "cart", "product", "product_name", "quantity"]

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ["id", "user", "created_at", "items"]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'created_at', 'status', 'items']

class CheckoutSerializer(serializers.Serializer):
    def create(self, validated_data):
        user = self.context['request'].user
        cart_items = CartItem.objects.filter(cart__user=user)

        if not cart_items.exists():
            raise serializers.ValidationError("Giỏ hàng trống!")

        order = Order.objects.create(user=user)
        order_items = []

        for item in cart_items:
            order_items.append(OrderItem(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            ))
        
        OrderItem.objects.bulk_create(order_items)
        cart_items.delete()  # Xóa giỏ hàng sau khi đặt hàng

        return order