<template>
    <div class="container">
        <div class="form">
            <form @submit.prevent="signup">
                <h1>ĐĂNG KÍ TÀI KHOẢN</h1>
                <div class="form-item">
                    <label class="title" for="username">Tên</label>
                    <input v-model="form.username" class="nhap" type="text" id="username">
                </div>
                <div class="form-item">
                    <label class="title" for="email">Email</label>
                    <input v-model="form.email" class="nhap" type="text" id="email">
                </div>
                <div class="form-item">
                    <label class="title" for="phone">Số điện thoại</label>
                    <input v-model="form.sdt" class="nhap" type="text" id="sdt">
                </div>
                <div class="form-item">
                    <label class="title" for="password">Mật khẩu</label>
                    <input v-model="form.password1" class="nhap" type="password" id="password">
                </div>
                <div class="form-item">
                    <label class="title" for="confirm">Xác nhận mật khẩu</label>
                    <input v-model="form.password2" class="nhap" type="password2" id="password2">
                </div>
                <div class="nut">
                    <button type="submit" class="gui">Đăng ký</button>
                </div>
                <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
            </form>
        </div>
    </div>
</template>

<script>
        import axios from "axios";

        export default {
            name: "Signup",
            data() {
                return {
                    form: {
                        email: "",
                        phone: "",
                        password: "",
                        password2: ""
                    },
                    errorMessage: "",
                };
            },
            methods: {
                async signup() {
            try {
                const csrfToken = this.getCookie("csrftoken");

                // Chuyển đổi dữ liệu: tạo username từ email và đổi password1 thành password
                const userData = {
                    username: this.form.email.split("@")[0],  // ví dụ: nếu email là "hien@gmail.com", username = "hien"
                    email: this.form.email,
                    phone: this.form.phone,
                    password: this.form.password1,
                    password2: this.form.password2
                };

                const response = await axios.post(
                    "http://127.0.0.1:8000/api/users/register/",
                    userData,
                    {
                        headers: {
                            "X-CSRFToken": csrfToken,
                            "Content-Type": "application/json",
                        },
                    }
                );

                if (response.status === 201) {
                    alert("Đăng ký thành công! Hãy đăng nhập.");
                    this.$router.push("/signin");
                }
            } catch (error) {
                console.error(error.response);
                this.errorMessage = error.response?.data?.error || "Có lỗi xảy ra!";
            }
        },

        getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== "") {
                const cookies = document.cookie.split(";");
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    if (cookie.startsWith(name + "=")) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
    }
};
</script>



<style>


/* form đăng kí tài khoản */

.input{
 
    text-align: center;
    border: none;
    font-size: 16px;
    margin-top: 50px;
}
.form {
    display: grid;
    margin-top: 200px;
    margin-left: 100px;
    background-color: RGB(255, 237, 237);
    border: solid 2px black;
    border-radius: 20px;
    padding: 20px;
    box-sizing: content-box;
    height: 300px;
    position: absolute;
    top: -43%;
    left: -13%;
    padding: 20px;

}

h1 {
    text-align: center;
  
}

.container {
    background-color: RGB(255, 237, 237);
    width: 600px;
    height: 400px;
    position: relative;
    display: flex;
    margin: auto;
   
}

.form-item {
    display: flex;
    margin: 15px;
    margin-bottom: 10px;
    padding: 0 16px;
    border-radius: 3px; 
    padding: 0 16px;
    border-radius: 3px;;
}

.title {
    font-size: 20px;
    margin-right: 10px;
    min-height: 20px;
    flex: 1;
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