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
                
            </div>
          </div>
</template>
<script>
const images = import.meta.glob('@/assets/IMG/*.jpg', { eager: true });

// Chuyển danh sách import thành một mảng đường dẫn ảnh
const imageList = Object.values(images).map(img => img.default);

console.log(imageList); // Kiểm tra danh sách ảnh được import
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
}
.cost{
   
   background-color: rgb(239, 226, 209);


}
</style>