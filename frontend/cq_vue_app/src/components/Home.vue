<template>
   <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
  <div class="wrapper">
  <header class="menu-toggle" >
  <!-- Mobile menu button -->
 
      <div class="navbar" >
          <div class="navbar-link" >
              <ul class="navbar-link-item"  :class="{ 'active': isOpen }">
                  <li class="item-link"> <a class="link" href="/"> Trang chủ</a></li>
                  <li class="item-link"> <a class="link" href="Product">Sản phẩm</a> </li>
                  <li class="item-link"> <a class="link" href="Blog"> About</a></li>
                  <li class="item-link"> <a class="link" href="contact">Liên hệ</a> </li>
              </ul>
          </div>
          <div class="navbar-logo">
              <img class="logo" src="@/assets/IMG/logo1.jpg" alt="logo">
          </div>
          <div class="navbar-search">
              <input type="text" class="search-input" placeholder="Tìm kiếm">
              <div class="icon-search">
                  <a class="link" href=""><i class="fa-solid fa-magnifying-glass"></i></a>
              </div>
          </div>
          <div class="navbar-cart-login-icon">
              <a style="font-size: 2rem;" href=""> <i  class="fa-solid fa-bag-shopping"></i></a>
              <a style="font-size: 2rem; padding-bottom: 10px;" href="signin"><i  class="fa-solid fa-user"></i></a>


          </div>
      </div>
      <div class="hamburger" @click="toggleMenu">☰</div>
 
</header>
</div>
<main>

<div class="banner">
  <section class="slider">
      <div class="slides">
          <img v-show="currentSlide === 1" class="banner-1" src="@/assets/IMG/bann1.jpg" alt="Hình 1">
          <img v-show="currentSlide === 2" class="banner-2" src="@/assets/IMG/bann2-1.jpg" alt="Hình 2">
      </div>
      <div class="button-container">
          <i @click="toggleSlide" class="fa-solid fa-arrow-right"></i>
      </div>
   </section> 
</div>

<div style="margin-bottom: 25px;" class="demo-product">
              <div class="demo-product">
                  <div class="demo-product-item">
                      <img class="img-demo" src="@/assets/IMG/ban-an.jpg" alt="Hình 1">
                  </div>
                  <div class="demo-product-item">
                      <img class="img-demo" src="@/assets/IMG/ban-an.jpg" alt="Hình 1">
                  </div>
                  <div class="demo-product-item">
                  <div class="box"><h3> Moda Casa</h3>  Nâng tầm phong cách sống với nội thất đẳng cấp, nơi mọi chi tiết đẳng cấp đều tạo nên sự khác biệt</div>
                   </div>
                  <div class="demo-product-item">
                      <img class="img-demo" src="@/assets/IMG/ban-an.jpg" alt="Hình 1">
                  </div>
                 
              
</div>
</div>

<!-- product -->
<div class="product">
          <p style="font-size: 2.5rem; margin: 0" class="title-product">Gợi ý cho bạn</p>
          <div class="product-item-contaner">
              <a href="/detail">
                  <div class="product-item">
                      <img class="img-product" src="@/assets/IMG/ban-an.jpg" alt="Hình 1">
                          <div class="cost"> <p  class="float" >Giường ngủ cao cấp<br><span style="color: red; padding-top: 15px">8200000</span></p>
                              <div class="evaluate">
                                  <ul class="evaluate_star" >
                                      <li> <i style="color:yellow" class="fa-solid fa-star"></i></li>
                                      <li> <i style="color:yellow" class="fa-solid fa-star"></i></li>
                                      <li> <i style="color:yellow" class="fa-solid fa-star"></i></li>
                                      <li> <i class="fa-solid fa-star"></i></li>
                                      <li> <i class="fa-solid fa-star"></i></li>
                                  </ul>
                                  <ul class="buy">
                                      <li>Đã bán 45</li>
                                  </ul>
                                  
                              </div> 
                      </div>
                  </div>
               </a>
               <a href="/detail">
              <div class="product-item">
                  <img class="img-product" src="@/assets/IMG/bn.jpg" alt="Hình 1">
                  <div class="cost"> <p  class="float" >Giường ngủ cao cấp<br><span style="color: red; padding-top: 15px">8200000</span></p>
                      <div class="evaluate">
                          <ul class="evaluate_star" >
                              <li> <i style="color:yellow" class="fa-solid fa-star"></i></li>
                              <li> <i style="color:yellow" class="fa-solid fa-star"></i></li>
                              <li> <i style="color:yellow" class="fa-solid fa-star"></i></li>
                              <li> <i class="fa-solid fa-star"></i></li>
                              <li> <i class="fa-solid fa-star"></i></li>
                          </ul>
                          <ul class="buy">
                              <li>Đã bán 45</li>
                          </ul>
                          
                      </div> 
              </div>
              </div>
              </a>
              <a href="/detail">
              <div class="product-item">
                  <img class="img-product" src="@/assets/IMG/ban-an.jpg" alt="Hình 1">
                   <div class="cost"> <p  class="float" >Giường ngủ cao cấp<br><span style="color: red; padding-top: 15px">8200000</span></p>
                          <div class="evaluate">
                              <ul class="evaluate_star" >
                                  <li> <i style="color:yellow" class="fa-solid fa-star"></i></li>
                                  <li> <i style="color:yellow" class="fa-solid fa-star"></i></li>
                                  <li> <i style="color:yellow" class="fa-solid fa-star"></i></li>
                                  <li> <i class="fa-solid fa-star"></i></li>
                                  <li> <i class="fa-solid fa-star"></i></li>
                              </ul>
                              <ul class="buy">
                                  <li>Đã bán 45</li>
                              </ul>
                              
                          </div> 
                  </div>
              </div>
              </a>
              <a href="/detail">
              
              <div class="product-item">
                  <img class="img-product" src="@/assets/IMG/bàn.jpg" alt="Hình 1">
                   <div class="cost"> <p  class="float" >Giường ngủ cao cấp<br><span style="color: red; padding-top: 15px">8200000</span></p>
                          <div class="evaluate">
                              <ul class="evaluate_star" >
                                  <li> <i style="color:yellow" class="fa-solid fa-star"></i></li>
                                  <li> <i style="color:yellow" class="fa-solid fa-star"></i></li>
                                  <li> <i style="color:yellow" class="fa-solid fa-star"></i></li>
                                  <li> <i class="fa-solid fa-star"></i></li>
                                  <li> <i class="fa-solid fa-star"></i></li>
                              </ul>
                              <ul class="buy">
                                  <li>Đã bán 45</li>
                              </ul>
                              
                          </div> 
                  </div>
              </div>
              </a>


              <a href="/detail">
              <div class="product-item">
                  <img class="img-product" src="@/assets/IMG/ban-an.jpg" alt="Hình 1">
                   <div class="cost"> <p  class="float" >Giường ngủ cao cấp<br><span style="color: red; padding-top: 15px">8200000</span></p>
                          <div class="evaluate">
                              <ul class="evaluate_star" >
                                  <li> <i style="color:yellow" class="fa-solid fa-star"></i></li>
                                  <li> <i style="color:yellow" class="fa-solid fa-star"></i></li>
                                  <li> <i style="color:yellow" class="fa-solid fa-star"></i></li>
                                  <li> <i class="fa-solid fa-star"></i></li>
                                  <li> <i class="fa-solid fa-star"></i></li>
                              </ul>
                              <ul class="buy">
                                  <li>Đã bán 45</li>
                              </ul>
                              
                          </div> 
                  </div>
              </div>
             </a>
             <a href="/detail">
              <div class="product-item">
                  <img class="img-product" src="@/assets/IMG/ban-an.jpg" alt="Hình 1">
                   <div class="cost"> <p  class="float" >Giường ngủ cao cấp<br><span style="color: red; padding-top: 15px">8200000</span></p>
                          <div class="evaluate">
                              <ul class="evaluate_star" >
                                  <li> <i style="color:yellow" class="fa-solid fa-star"></i></li>
                                  <li> <i style="color:yellow" class="fa-solid fa-star"></i></li>
                                  <li> <i style="color:yellow" class="fa-solid fa-star"></i></li>
                                  <li> <i class="fa-solid fa-star"></i></li>
                                  <li> <i class="fa-solid fa-star"></i></li>
                              </ul>
                              <ul class="buy">
                                  <li>Đã bán 45</li>
                              </ul>
                              
                          </div> 
                  </div>
              </div>
              </a>
              <a href="/detail">
              <div class="product-item">
                  <img class="img-product" src="@/assets/IMG/bn.jpg" alt="Hình 1">
                   <div class="cost"> <p class="float" >Giường ngủ cao cấp<br><span style="color: red; padding-top: 15px">8200000</span></p>
                          <div class="evaluate">
                              <ul class="evaluate_star" >
                                  <li> <i style="color:yellow" class="fa-solid fa-star"></i></li>
                                  <li> <i style="color:yellow" class="fa-solid fa-star"></i></li>
                                  <li> <i style="color:yellow" class="fa-solid fa-star"></i></li>
                                  <li> <i class="fa-solid fa-star"></i></li>
                                  <li> <i class="fa-solid fa-star"></i></li>
                              </ul>
                              <ul class="buy">
                                  <li>Đã bán 45</li>
                              </ul>
                              
                          </div> 
                  </div>
              </div>
              </a>
              <a href="/detail">
              
              <div class="product-item">
                  <img class="img-product" src="@/assets/IMG/bàn.jpg" alt="Hình 1">
                   <div class="cost"> <p  class="float" >Giường ngủ cao cấp<br><span style="color: red; padding-top: 15px">8200000</span></p>
                          <div class="evaluate">
                              <ul class="evaluate_star" >
                                  <li> <i style="color:yellow" class="fa-solid fa-star"></i></li>
                                  <li> <i style="color:yellow" class="fa-solid fa-star"></i></li>
                                  <li> <i style="color:yellow" class="fa-solid fa-star"></i></li>
                                  <li> <i class="fa-solid fa-star"></i></li>
                                  <li> <i class="fa-solid fa-star"></i></li>
                              </ul>
                              <ul class="buy">
                                  <li>Đã bán 45</li>
                              </ul>
                              
                          </div> 
                  </div>
              </div>
              </a>
              
          </div>
        </div>
       
  <footer>
      <div class="container-footer">
          <p class="title-footer">Vì sao nên chọn Moda Casa</p>

          <div >
              <div class="feature-footer" >
                  
                          <div class="feature-footer-item">
                              <i class="icon-feature fa-solid fa-truck-fast"></i>
                              <p class="text-feature">Giao hàng và lắp đặt miễn phí</p>
                          </div>
                      
                          <div class="feature-footer-item">
                              <i class="icon-feature fa-solid fa-arrows-rotate"></i>
                              <p class="text-feature">30 ngày đổi trả miễn phí</p>
                          </div>
                     
                          <div class="feature-footer-item">
                              <i class="icon-feature fa-solid fa-headphones"></i>
                              <p class="text-feature">Tư vấn thiết kế miễn phí</p>
                          </div>
                      
                         
                          <div class="feature-footer-item">
                              <i class="icon-feature fa-solid fa-circle-check"></i>
                              <p class="text-feature">Thương hiệu uy tín toàn cầu</p>
                          </div>
                   
              </div>
         </div>
      </div>


      <div class="blog-footer">
              <div style="padding-left: 1.7rem;" class="side sidebar1">
                  <p class="header-feature"> Moda Casa</p>
                  <p style="   line-height: 30px;
                              padding-top: 1rem;
                                  " class="text-header-feature">
              Nội thất Moda Casa là thương hiệu đến từ Việt Nam với hơn 20 năm kinh nghiệm trong việc sản xuất và xuất khẩu nội thất đạt chuẩn quốc tế</p>
              </div>
              <div class="side sidebar2">
                  <p style="    padding-left: 1rem;" class="header-feature">Dịch vụ</p>
                  <ul style="line-height: 30px;
                              padding-top: 1rem;
                              " class="text-header-feature">
                      <li>Chính sách bán hàng</li>
                      <li>Chính sách giao hàng & lắp đặt</li>
                      <li>Chính sách bảo hàng & bảo trì</li>
                      <li>Chính sách đổi trả</li>
                  </ul>
              </div>
              <div class="side sidebar3">
                  <p style="padding-left: 2rem;" class="header-feature">Thông tin liên hệ</p>
                  <ul class="text-header-feature">
                      <li class="text-header-feature-item">
                          <i  class="icon-item fa-solid fa-location-dot"></i>
                          <p>Địa chỉ: 140 đường Nguyễn Hữu Thọ, quận 7, TP.HCM</p>
                      </li>
                      <li class="text-header-feature-item">
                          <i  class="icon-item fa-solid fa-phone-volume"></i>
                          <p>0878786523</p>
                      </li>
                      <li class="text-header-feature-item">
                          <i  class="icon-item fa-regular fa-envelope"></i>
                          <p>cskh@gmail.vn</p>
                      </li>
                  </ul>
              </div>
          </div>
       
</footer>
</main> 
<div>
  <button @click="buyProduct">Mua ngay</button>
</div>
</template>  
  <script>
  import { ref } from "vue";
  
  const images = import.meta.glob('@/assets/IMG/*.jpg', { eager: true });
  const imageList = Object.values(images).map(img => img.default);
  
  export default {
    setup() {
      const currentSlide = ref(0);
      const products = ref([
        { name: "Giường ngủ cao cấp", image: "@/assets/IMG/ban-an.jpg", price: "8.200.000", rating: 4, sold: 45 },
        { name: "Bàn ăn gỗ", image: "@/assets/IMG/bn.jpg", price: "5.500.000", rating: 5, sold: 30 }
      ]);
  
      const toggleSlide = () => {
        currentSlide.value = (currentSlide.value + 1) % imageList.length;
      };
  
      const buyProduct = () => {
        const token = localStorage.getItem("access_token");
        if (!token) {
          alert("Bạn cần đăng nhập trước khi mua hàng!");
          window.location.href = "/signin";
        } else {
          alert("Mua hàng thành công!");
        }
      };
  
      return { currentSlide, toggleSlide, buyProduct, imageList, products };
    },
    data() {
    return {
      currentSlide: 1, // Bắt đầu từ slide 1
      totalSlides: 2   // Có tổng cộng 2 slide
    };
  },
  mounted() {
    // Chuyển tự động sang slide 2 sau 5 giây
    setTimeout(() => {
      this.currentSlide = 2;
    }, 5000);
  },
  methods: {
    nextSlide() {
      console.log("Before Click:", this.currentSlide);
      this.currentSlide = this.currentSlide === 1 ? 2 : 1;
      console.log("After Click:", this.currentSlide);
    }
  }
    
  };
  </script>



<style>
main{
    padding-top: 50px;
}   



@media screen and (max-width: 800px) 
{

    .navbar-search{
        display: none !important;
    }
    .search-input{
        display: none;
    }
    .navbar-cart-login-icon{
        display: none !important;
    }
    .navbar-logo{

        display: none;
    }

    main{
    padding-top: 200px;
  }
  .navbar-link {
   
   
    background-color: var(--color-primary);
    width: 100% !important;; /* Chiều rộng 100% */
    /* padding-top: 30px; */
    position: fixed; /* Tuyệt đối */
    top: 20px; /* Cách top 50px */
    left: 0; /* Cách trái 0px */
    right: 0;
    flex-wrap: wrap;
  }
  .navbar-link-item {
    flex-direction: column;
    align-items: center; /* Căn giữa nội dung */
   
  }
   
  .navbar-link-item.active {
     display: flex;
    
    }

 
}



.banner {
  margin-top: 20px;
}
.slider {
  position: relative;
  max-width: 100%;
  overflow: hidden;
}

.slides img {
  width: 100%;
  transition: opacity 0.5s ease-in-out;
}

.button-container {
  position: absolute;
  top: 50%;
  right: 20px;
  transform: translateY(-50%);
  cursor: pointer;
  font-size: 24px;
  color: black;
  background: rgba(255, 255, 255, 0.5);
  padding: 10px;
  border-radius: 50%;
}


*{
   
   /* padding: 0; */
   box-sizing: border-box;
 
}


body{
   background-color: RGB(243, 238, 234);
}
:root{
   /* màu nâu */
   --color-primary: RGB(138, 99, 68);


   --background-color: RGB(216, 206, 199);
}


/* header */
.navbar{
   width: 100%;
   height:50px;
   background-color: var(--color-primary);
   display: flex;
   align-items: center;
   font-size: 1.75rem;
   border-radius: 10px;
   position: fixed;  /* Cố định menu trên cùng */
    top: 0;           /* Gán vị trí trên cùng */
    left: 0;
    width: 100%;      /* Kéo dài toàn bộ chiều rộng */
    z-index: 1000;  /* Đặt lớp z-index cao nhất */
   
  

}




.navbar-link-item{
   display: flex;
   justify-content: space-between;
   margin: 0 ;
   font-size: 1.5rem;


}


.item-link{
   list-style: none;
   margin: 0 20px;


}
.link{
   text-decoration: none;
   color: rgb(37, 36, 36);
   font-size: 1.5rem;


}


.logo{
   width: 175px;
   height: 38px;
   margin-right: 40px;
}


.navbar-search{


  display: flex;
  background-color: white;;
  border-radius: 15px;
  outline-color: white;
  width: 35rem;


}
.search-input{
   border-style: none;
   border-radius: 15px;
   padding: 0 10px;
   width: 30rem;
}
.icon-search{
   border-left: 2px solid #3333;
   padding: 3px 20px;
   width: 5rem;
   
   
}
.navbar-cart-login-icon{
   margin: 1rem;
   margin: 1rem;
    display: flex;
    align-items: center;



}
.fa-bag-shopping{
   margin: 1rem;
}


/* main */


/* main{
   margin-top: 30px;
} */
.slider{
   width: 100%;
   height: 500px;;
   position: relative;
}
.banner-1{
   width: 100%;
   height: 500px;
   border-radius: 10px;
   
   
}



.button-container{
   display: flex;
   justify-content: space-between;
   color:rgb(105, 105, 104);
   font-size: 3rem;
   position:absolute ;
   top: 50%;
   right: 0;




}
.banner-2{
   width: 100%;
   height: 500px;
    border-radius: 10px;


}


/* demo product */


.demo-product{
    margin-top: 20px;
   display: flex;
   justify-content: space-between;
   flex-wrap: wrap;
   margin-left: 5px;
   
   
    
   
}
.demo-product-item{
   display: flex;
   justify-content: space-around;
   margin: 0 25px;
  

}


.img-demo{
    max-width: 315px;
    min-height: 10%;
    border-radius: 5px;
    margin-left: 9px;
}


.box{
   background-color: var(--color-primary);
   color: RGB(243, 238, 234);
   width: 20rem;
   height: 20rem;
   font-size: 1.5rem;
   line-height: 10px;
   margin-top: 5px;
   line-height: 2rem;
   padding:10px;
   border-style: 5px solid RGB(243, 238, 234);
   border-radius: 5px;


}
h3{
   margin:0;
   padding-bottom: 10px;


}


/* product */

.product {
   margin-top: 70px;
   
}


.title-product{
   margin-bottom: 0;
   background-color: rgb(234, 206, 172);
   padding: 0.5rem;
   


}
.img-product{
   width: 20rem;
   height: 18rem;
 
}


.product-item{
   margin-top: 30px;
   padding: 5px;
}


.product-item-contaner{
   display: flex;
   flex-wrap: wrap;
   justify-content: space-around;
  


}


.evaluate{
   display: flex;
   justify-content: space-between;
   padding: 0 10px;
}


.buy{
   display: flex;
   list-style: none;
   font-size: 1.1rem;
}
.evaluate_star{
   display: flex;
   list-style: none;
   padding: 0;
}


.float{
   padding: 10px;
   margin: 0;
   font-size: 1.3rem;
   text-align: left;
}
.cost{
   
   background-color: rgb(239, 226, 209);


}


/* footer */
footer{
   margin-top: 70px;
   
}


.title-footer{
   text-align: center;
   font-size: 2rem;
   background-color: RGB(138, 99, 68);
   padding: 12px;
   color: white;


}


.feature-footer{
    margin-top: 50px;
   display: flex;
   justify-content: space-around;
    flex-wrap: wrap;

   
}


.text-feature{
   text-align: center;
   font-size: 1.7rem;
   font-weight: 400;


}

.feature-footer-item{
   background-color:RGB(239, 226, 209);
   width: 20rem;
   height: 15rem;
   border: 5px solid #7a5b2f;
   font-weight: 900;
   font-size: 1.3rem;
 
}
.icon-feature{
   text-align: center;
   font-size: 3rem;
   margin: 3rem 8rem;
}


.blog-footer{
   display: flex;
   justify-content: space-around;
   margin: 0 3rem;
   flex-wrap: wrap;
   flex-basis: 40%;
}
  
/* .sidebar1{
 
 




}
.sidebar2{
 
   


}
.sidebar3{
   
   
   


} */
.header-feature{
   font-size: 2rem;
   font-weight: 800;
}
.side{
   padding: 10px;
   height: 20rem;
   margin-top: 3rem;
   width: 20rem;

  
}
.text-header-feature{
   font-size: 1.2rem;
   margin-top: 16px;
}
.text-header-feature-item{
   display: flex;
   padding: 10px;
   line-height: 30px;
   
}
.icon-item {
   margin-right: 20px;
   
   text-align: center;
   align-items: center;
   display: flex;
   padding-top: 7px;


}

</style>