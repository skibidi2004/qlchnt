<template>
    <div style="height: 375px" class="container-sig">

<div   class="form-sig">
    <form @submit.prevent="signup" action="" method="POST" >
        <h1>THÔNG TIN ĐĂNG NHẬP</h1>
        <div class="input">
            <div class="form-item-sig">
            
                <label 
             class="title-sig" for="username">Tên đăng nhập</label>
            <input v-model="form.name" style="  padding: 0 16px;" class="nhap" type="text" name="email" id="username" >
            </div>
            <div class="form-item">
            
                <label   class="title-sig" for="password">Mật khẩu</label>
                <input v-models="form.name"  style="  padding: 0 16px;"  class="nhap" type="password" name="password" id="password" >
            </div>
        </div>
        <div  style="margin-top: 20px;" class="controls">
            <div @click="signin()" style="margin-bottom: 4px; "  class="nut" >
                <button style=" 
                padding: 8px 16px;
                border-radius: 5px;
                background-color: RGB(167, 110, 67);
                border: 1px solid RGB(167, 110, 67);
                 display: flex; 
                margin: auto;
                margin-top: 5px;
                font-size: 1rem;
                color: white;
                  
                 " class="gui" type="submit">Đăng nhập</button>
            </div>
            <div   class="forgot"> <a style="color: #807373; text-decoration: underline; padding-bottom: 1px;  font-size: 1rem;                                             
                " href=""
                >Quên mật khẩu</a></div>
        </div>
        
    </form>

</div>
</div>
</template>

<script>
export default {
    name: 'signin',
    data() {
        return {
            form: {
                name: '',
                password: ''
            }
        }
    },
    methods: {
       signin() {
           console.log(this.form);
       }
    }
} 
</script>

<style>


/* form đăng kí tài khoản */


.form-sig {
    display: grid;
    margin-top: 200px;
    margin-left: 100px;
    background-color: RGB(231, 218, 202);
    border: solid 2px black;
    border-radius: 20px;
    padding: 20px;
    box-sizing: content-box;
    height: 300px;
    position: absolute;
    top: -49%;
    left: -14.5%;
    padding: 20px;
    

}

h1 {
    text-align: center;
  
}

.input{
    min-width: 516px;
}
.container-sig {
    background-color: RGB(231, 218, 202);
    width: 600px;
    height: 400px;
    position: relative;
    display: flex;
    margin: auto;
   
}

.form-item-sig {
    display: flex;
    margin: 15px;
    margin-bottom: 10px;
    padding: 0 16px;
    border-radius: 3px; 
    padding: 0 16px;
    border-radius: 3px;;
}

.title-sig {
    font-size: 20px;
   
    min-height: 20px;
    flex: 1;
    min-width: 200px;   /* Giữ độ rộng cố định cho label */
    text-align: left;
    
}

.nhap {
    min-width: 270px;
    height: 30px;
border-radius: 5px;
    border: solid 1px black;
    flex: 1;
    border-radius: 30px;
  
    
}

.nut {
    border-radius: 20px;
    min-width: 150px;
    
    min-height: 45px;
    font-size: 20px;
    cursor: pointer;
    width: 100px;
    height: 30px;
    margin: 15px auto;

}

.forgot,a {
    display: block;
    padding-top: 1px;
    color: black;
    text-align: center;  
    font-size: 1rem;
   
}

button.gui {
    padding: 8px 16px;
    border-radius: 5px;
    background-color: RGB(255, 195, 213);
    border: 1px solid RGB(255, 195, 213);
    margin-top: 5px;
}


.forgot{
    font-size: 0.5rem;
    color: #807373;

}

.controls{
    color: #646c6c9c;
}

.border{
    border-bottom: 1px solid;
}

@media (min-width: 1024px) {
  #app {
    grid-template-columns: unset !important;
  }
}


</style>