<template>
    <div class="cart-container">
      <h1>🛒 Giỏ Hàng Của Bạn</h1>
  
      <div v-if="cart.length === 0" class="empty-cart">
        <p>Giỏ hàng của bạn đang trống!</p>
        <router-link to="/products" class="back-to-shop">🛍️ Tiếp tục mua sắm</router-link>
      </div>
  
      <div v-else>
        <table class="cart-table">
          <thead>
            <tr>
              <th>Sản phẩm</th>
              <th>Giá</th>
              <th>Số lượng</th>
              <th>Tổng</th>
              <th>Hành động</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in cart" :key="item.id">
              <td class="cart-item">
                <img :src="getProductImage(item)" alt="Product image" class="cart-image">
                <span>{{ item.name }}</span>
              </td>
              <td>{{ formatPrice(item.price) }}</td>
              <td>
                <button @click="updateQuantity(item, -1)">➖</button>
                <span>{{ item.quantity }}</span>
                <button @click="updateQuantity(item, 1)">➕</button>
              </td>
              <td>{{ formatPrice(item.price * item.quantity) }}</td>
              <td><button @click="removeFromCart(item)">❌ Xóa</button></td>
            </tr>
          </tbody>
        </table>
  
        <div class="cart-total">
          <h2>Tổng tiền: {{ formatPrice(totalPrice) }}</h2>
          <button @click="checkout" class="checkout-button">🛍️ Thanh Toán</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        cart: [], // Lưu trữ danh sách sản phẩm trong giỏ hàng
      };
    },
    computed: {
      totalPrice() {
        return this.cart.reduce((total, item) => total + item.price * item.quantity, 0);
      },
    },
    methods: {
      getProductImage(product) {
        if (product.images && product.images.length > 0) {
          return `http://127.0.0.1:8000${product.images[0].image_url}`;
        }
        return "/default-image.jpg"; // Ảnh mặc định nếu không có ảnh
      },
      formatPrice(price) {
        return new Intl.NumberFormat("vi-VN", { style: "currency", currency: "VND" }).format(price);
      },
      updateQuantity(item, change) {
        const index = this.cart.findIndex((p) => p.id === item.id);
        if (index !== -1) {
          this.cart[index].quantity += change;
          if (this.cart[index].quantity <= 0) {
            this.cart.splice(index, 1);
          }
          this.saveCart();
        }
      },
      removeFromCart(item) {
        this.cart = this.cart.filter((p) => p.id !== item.id);
        this.saveCart();
      },
      saveCart() {
        localStorage.setItem("cart", JSON.stringify(this.cart));
      },
      checkout() {
        alert("Chức năng thanh toán đang phát triển!");
      },
    },
    created() {
      this.cart = JSON.parse(localStorage.getItem("cart")) || [];
    },
  };
  </script>
  
  <style>
  .cart-container {
    max-width: 800px;
    margin: auto;
    padding: 20px;
    text-align: center;
  }
  .cart-table {
    width: 100%;
    border-collapse: collapse;
  }
  .cart-table th, .cart-table td {
    border: 1px solid #ddd;
    padding: 10px;
  }
  .cart-image {
    width: 50px;
    height: auto;
  }
  .cart-total {
    margin-top: 20px;
    font-size: 1.2rem;
  }
  .checkout-button {
    background-color: #ff6600;
    color: white;
    padding: 10px;
    border: none;
    cursor: pointer;
    font-size: 1.2rem;
  }
  .empty-cart {
    font-size: 1.2rem;
  }
  .back-to-shop {
    display: inline-block;
    margin-top: 10px;
    font-size: 1rem;
    color: blue;
  }
  </style>
  