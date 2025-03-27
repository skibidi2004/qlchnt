<template>
  <div id="app">
    <!-- Khu vực hiển thị component tương ứng với route -->
    <router-view />
  </div>
</template>

<script setup>
/* 
  Thông thường, App.vue không import router. 
  Việc 'use(router)' sẽ được thực hiện trong main.js.
*/
</script>

<style>
body {
  background-color: white;
  color: black; /* Đổi màu chữ để dễ nhìn hơn */
  margin: 0;
  padding: 0;
  font-family: sans-serif;
}
</style>
