<template>
    <div class="buy-now">
        <div style="background-color: RGB(242, 239, 234); border-right: 1px solid black" class="buy-now-item">
            <h1 class="buy-now-item__title">Nội thất Modo Casa</h1>
           <div class="buy-now-item__form">
                <h2 class="header--inf">Thông tin giao hàng</h2>
            <div class="buy-now-item__form--inf">
                <div class="name-gender">
                    <input type="text" class="form-gender input-buy-now input--name--buy-now" placeholder="Họ và tên">
                    <div class="form-gender">
                        <label for="">nữ</label>
                        <input name="gender" type="radio" class="input--choose--gender">
                        <label class="label-gender-man" for="">nam</label>
                        <input name="gender" type="radio" class="input--choose--gender">
                    </div>
                 </div>
                <div class="email-phone">
                    <input type="text" class="input-buy-now input--email--buy-now" placeholder="Email">
                    <input type="text" class="input-buy-now input--phone--buy-now" placeholder="Số điện thoại">
                </div>  
                <input type="text" class="input-buy-now input--address--buy-now" placeholder="Địa chỉ">
            </div>
            <div class="buy-now-item__form--move">
                <h2 class="header--inf">Phương thức vận chuyển</h2>
                <div class="input-choose">
                    <input name="move" type="radio" class="input--choose--buy-now" >
                    <label class="label-choose" for="">Giao hàng nhanh</label>
                </div>
                 <div class="input-choose">
                    <input name="move" type="radio" class="input--choose--buy-now">
                    <label class="label-choose" for="">J&T Express</label>
                </div>
                 <div class="input-choose">
                    <input name="move" type="radio" class="input--choose--buy-now">
                    <label class="label-choose" for="">Giao hàng tiết kiệm</label>
                </div>
                   
            </div>
            <div class="buy-now-item__form--move">
                <h2 class="header--inf">Phương thức thanh toán</h2>
                <div class="input-choose">
                    <input name="move" type="radio" class="input--choose--buy-now" >
                    <label class="label-choose" for="">Thanh toán khi nhận hàng</label>
                </div>
                 <div class="input-choose">
                    <input name="move" type="radio" class="input--choose--buy-now">
                    <label class="label-choose" for="">Thanh toán chuyển khoản qua ngân hàng</label>
                </div>
                 <div class="input-choose">
                    <input name="move" type="radio" class="input--choose--buy-now">
                    <label class="label-choose" for="">Ví MoMo</label>
                </div>
                   
            </div>
           </div>
        </div>
        <div class="buy-now-item">
            <div class="scrollbar" id="style-1">
                <div class="force-overflow">
      <!-- Danh sách sản phẩm -->
    
             <div class="img-package-container">
                        <div class="buy-now-item__img--package">
                            <img src="@/assets/IMG/bàn.jpg" alt="" class="img--package">
                            <div class="amount-img-package">2</div>
                        </div>
                        <div class="buy-now-item__name--package">
                             <p class="name--package">Tủ giày - Tủ thơi trang trí bằng gỗ</p>
                         </div>
                        <div class="buy-now-item__cost--package">
                            <p class="cost--package">150000000</p>
                        </div>
                </div>
             <div class="img-package-container__hai">
                        <div class="buy-now-item__img--package">
                            <img src="@/assets/IMG/bàn.jpg" alt="" class="img--package">
                            <div class="amount-img-package">2</div>
                        </div>
                        <div class="buy-now-item__name--package">
                             <p class="name--package">Tủ giày - Tủ thơi trang trí bằng gỗ</p>
                         </div>
                        <div class="buy-now-item__cost--package">
                            <p class="cost--package">150000000</p>
                        </div>
                </div>
             <div class="img-package-container__hai">
                        <div class="buy-now-item__img--package">
                            <img src="@/assets/IMG/bàn.jpg" alt="" class="img--package">
                            
                            <div class="amount-img-package">2</div>
                        </div>
                        <div class="buy-now-item__name--package">
                             <p class="name--package">Tủ giày - Tủ thơi trang trí bằng gỗ</p>
                         </div>
                        <div class="buy-now-item__cost--package">
                            <p class="cost--package">150000000</p>
                        </div>

                        
                </div>
            </div>
            </div>
    
                <hr>
                <div class="payment-detail-container">
            <h2 class="header--inf">Chi tiết thanh toán</h2>
            <div class="payment-detail-content">
                <div class="payment-detail-content__item">
                    <p class="payment-detail-content__item--name">Tạm tính</p>
                    <p class="payment-detail-content__item--cost">150000000</p>
                </div>
                <div class="payment-detail-content__item">
                    <p class="payment-detail-content__item--name">Phí vận chuyển</p>
                    <p class="payment-detail-content__item--cost">2000000</p>
                </div>
                <div class="payment-detail-content__item">
                    <p class="payment-detail-content__item--name">Tổng cộng</p>
                    <p class="payment-detail-content__item--cost">152000000</p>
                </div>
    
                <button type="submit" class="button-order" ><a class="order" href="">ĐẶT HÀNG</a></button>
    
            
        </div>
    
        
    </div>
        </div>
    </div>
    </template>
    <script>
    </script>
    <style>
    .scrollbar {
        background-color:RGB(252, 248, 239);
        float: left;
        height: 300px;
        margin-bottom: 25px;
        margin-left: 22px;
        margin-top: 40px;
        max-width: 100%;
        overflow-y: scroll;
    }
    
    .force-overflow {
        min-height: 450px;
    }
    .button-order{
        border-style: none;   
        display: flex;
        margin: 50px auto;
        border-radius: 15px;
        background-color: RGB(151, 99, 62);
    }
    .buy-now-item__title{
        font-size: 2rem;
        font-weight: 500;
    }
    .order{
        border-radius: 15px;
        background-color: RGB(151, 99, 62);
        color: white;
        text-decoration: none;
        padding: 10px 20px;
    }
    .payment-detail-content__item{
        margin: 15px;
    }
    .payment-detail-content__item--cost{
        color: brown;
    }
    .buy-now-item__cost--package{
        font-size: 1.2rem;
        color: brown;
    }
    .img-package-container__hai{
        margin-top: 20px;
        display: flex;
    }
    .input-choose{
        border: 1px solid black;
        max-width: 100%;
        border-radius: 15px;
        padding: 5px 10px;
        margin: 20px 0;
        font-size: 1.2rem;
    
    }
    .name--package{
        min-width: 150px;
    }
    .label-gender-man{
        margin-left: 10px;
    }
    .input--choose--gender{
        margin-left: 10px;
    }
    .form-gender{
      margin: 0 10px;
      font-size: 1.4rem;
    }
    .name-gender{
        display: flex;
        justify-content: space-between;
    }
    .payment-detail-content__item{
        display: flex;
        justify-content: space-between;
        font-size: 1.2rem;
    }
    .header--inf{
        padding: 5px 10px;
        max-width: 100%;
        text-align: center;
        background-color: RGB(213, 184, 152);
        border-radius: 5px;
        margin: 10px 0;
    }
    .label-choose{
        margin-left: 5px;
    }
    .input--address--buy-now{
        width: 100%;
    }
    .input-buy-now{
        padding: 5px 16px;
        margin: 5px 3px;
        border-radius: 15px;
        border: 1px solid #989696;
        font-size: 1.2rem;
        background-color: RGB(242, 239, 234);
        color:black;
    
    }
    .img-package-container{
        display: flex;
        
    }
    .email-phone{
        display: flex;
    }
    /* .buy-now-item__form--inf{
     
    } */
    .buy-now-item__form{
       background-color: RGB(242, 239, 234); 
    }
    /* .input--name--buy-now{
       
    
    } */
    .buy-now-item__name--package{
        max-width: 150px;
        font-size: 1.2rem;
    }
    
    .img-package-container{
        margin-top: 20px
    }
    .buy-now-item__img--package{
        position: relative;
        margin-right: 20px;
      
    }
    .buy-now-item{
        /* display: flex; */
        padding: 12px 20px;
       
      
    
    }
    .buy-now{
        display: flex;
        background-color: RGB(252, 248, 239);
        flex-wrap: wrap;
    
    }
    .amount-img-package{
        position: absolute;
        top: -10%;
        right: -8%;
        background-color: RGB(135, 100, 68);
        color: #fff;
        padding: 2px 8px;
        
        border-radius: 100%;
    }
    .img--package{
        width: 100px;
        height: 100px;
        position: relative;
    }
    hr{
       width:85%;
        border: 1px solid rgb(117, 110, 110);
        margin: 20px auto;
    
    }
    </style>