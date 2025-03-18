<template>
    <div class="product-list">
      <h1 class="title">Danh Sách Sản Phẩm</h1>
      
      <div v-if="loading" class="loading">Đang tải sản phẩm...</div>
      <div v-else-if="error" class="error">{{ error }}</div>
      <div v-else class="products-container">
        <div v-for="product in products" :key="product.id" class="product-card" @click="goToProductDetail(product.id)">
          <img class="product-image" :src="product.image" :alt="product.name" />
          <div class="product-info">
            <h3>{{ product.name }}</h3>
            <p class="price">{{ formatPrice(product.price) }}</p>
            <p>Đã bán: {{ product.sold }}</p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        products: [], // Danh sách sản phẩm từ API
        loading: true,
        error: null
      };
    },
    methods: {
      async fetchProducts() {
        try {
          const response = await axios.get("http://127.0.0.1:8000/api/products/");
          this.products = response.data;
        } catch (error) {
          this.error = "Lỗi khi tải sản phẩm! Vui lòng thử lại.";
        } finally {
          this.loading = false;
        }
      },
      goToProductDetail(productId) {
        this.$router.push(`/products/${productId}`);
      },
      formatPrice(price) {
        return new Intl.NumberFormat("vi-VN", { style: "currency", currency: "VND" }).format(price);
      }
    },
    created() {
      this.fetchProducts();
    }
  };
  </script>
  
  <style scoped>
  .product-list {
    text-align: center;
    padding: 20px;
  }
  
  .products-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
  }
  
  .product-card {
    width: 220px;
    border: 1px solid #ddd;
    padding: 10px;
    border-radius: 5px;
    cursor: pointer;
    transition: transform 0.2s;
  }
  
  .product-card:hover {
    transform: scale(1.05);
  }
  
  .product-image {
    width: 100%;
    height: auto;
    border-radius: 5px;
  }
  
  .product-info {
    text-align: left;
  }
  
  .price {
    color: red;
    font-weight: bold;
  }
  </style>
  