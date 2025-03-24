<template>
  <div class="product-list">
    <h1 class="title">Danh Sách Sản Phẩm</h1>
    <div class="filters">
      <input type="text" v-model="searchQuery" placeholder="Tìm kiếm sản phẩm..." @input="fetchProducts" />
      <select v-model="selectedCategory" @change="fetchProducts">
        <option value="">Tất cả danh mục</option>
        <option v-for="category in categories" :key="category.id" :value="category.id">{{ category.name }}</option>
      </select>
      <input type="number" v-model="minPrice" placeholder="Giá tối thiểu" @input="fetchProducts" />
      <input type="number" v-model="maxPrice" placeholder="Giá tối đa" @input="fetchProducts" />
    </div>

    <div v-if="loading">Đang tải sản phẩm...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <div v-else class="products-container">
      <div v-for="product in products" :key="product.id" class="product-card">
        <img class="product-image" :src="getProductImage(product)" :alt="product.name" @click="goToProductDetail(product.id)" />
        <div class="product-info">
          <h3 @click="goToProductDetail(product.id)">{{ product.name }}</h3>
          <p class="price">{{ formatPrice(product.price) }}</p>
          <p>Đã bán: {{ product.sold }}</p>
          <button class="cart-button" @click.stop="addToCart(product)">
            🛒 Thêm vào giỏ
          </button>
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
      products: [],
      categories: [],
      searchQuery: "",
      selectedCategory: "",
      minPrice: "",
      maxPrice: "",
      loading: true,
      error: null,
      cart: [], // Lưu trữ giỏ hàng
    };
  },
  methods: {
    async fetchProducts() {
      this.loading = true;
      try {
        const params = {
          category: this.selectedCategory,
          search: this.searchQuery,
          min_price: this.minPrice,
          max_price: this.maxPrice,
        };
        const response = await axios.get("http://127.0.0.1:8000/api/products/", { params });
        this.products = response.data;
      } catch (err) {
        this.error = "Lỗi khi tải sản phẩm!";
      } finally {
        this.loading = false;
      }
    },
    async fetchCategories() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/categories/");
        this.categories = response.data;
      } catch (err) {
        console.error("Lỗi khi tải danh mục sản phẩm", err);
      }
    },
    getProductImage(product) {
  if (product && product.images && product.images.length > 0) {
    let imageUrl = product.images[0].image_url;

    // Kiểm tra nếu đường dẫn đã đúng format thì giữ nguyên
    if (imageUrl.startsWith("http")) {
      return imageUrl;
    }

    // Chuẩn hóa đường dẫn nếu Django trả về URL tương đối
    return `http://127.0.0.1:8000/product_images/${imageUrl.split('/').pop()}`;
  }

  return "/default-image.jpg"; // Ảnh mặc định nếu không có ảnh
},

    goToProductDetail(productId) {
      this.$router.push(`/products/${productId}`);
    },
    formatPrice(price) {
      return new Intl.NumberFormat("vi-VN", { style: "currency", currency: "VND" }).format(price);
    },
    addToCart(product) {
      let cart = JSON.parse(localStorage.getItem("cart")) || [];
      let existingItem = cart.find((item) => item.id === product.id);
      
      if (existingItem) {
        existingItem.quantity += 1;
      } else {
        cart.push({ ...product, quantity: 1 });
      }

      localStorage.setItem("cart", JSON.stringify(cart));
      this.cart = cart;
      alert("Đã thêm vào giỏ hàng!");
    },
  },
  created() {
    this.fetchProducts();
    this.fetchCategories();
    this.cart = JSON.parse(localStorage.getItem("cart")) || [];
  },
};
</script>
<style>
.product-list {
  padding: 1rem;
}

.title {
  text-align: center;
  margin-bottom: 1rem;
  background-color: rgb(234, 206, 172);
  padding: 0.5rem;
}

.filters {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 1rem;
}

.filters input, .filters select {
  padding: 0.5rem;
  font-size: 1rem;
}

.products-container {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  justify-content: center;
}

.product-card {
  border: 1px solid #ccc;
  padding: 1rem;
  width: 20rem;
  text-align: center;
  cursor: pointer;
  position: relative;
}

.product-image {
  width: 100%;
  height: auto;
}

.product-info h3 {
  margin: 0.5rem 0;
}

.price {
  color: red;
  font-weight: bold;
}

.error {
  color: red;
  text-align: center;
}

.cart-button {
  margin-top: 10px;
  padding: 8px;
  background-color: #ff6600;
  color: white;
  border: none;
  cursor: pointer;
  font-weight: bold;
  border-radius: 5px;
}

.cart-button:hover {
  background-color: #ff4500;
}
</style>
