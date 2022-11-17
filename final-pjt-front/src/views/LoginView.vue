<template>
    <div>
      <h1>Login</h1>
      <div>
        <label for="username">사용자 이름: </label>
        <input type="text" id="username" v-model="credentials.username" />
      </div>
      <div>
        <label for="password">비밀번호: </label>
        <input
          type="password"
          id="password"
          v-model="credentials.password"
          @keyup.enter="login"
        />
      </div>
      <button @click="login">로그인</button>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    name: "LoginView",
    data: function() {
      return {
        credentials: {
          username: null,
          password: null,
        },
      };
    },
    methods: {
      login: function() {
        axios({
          method: "post",
          url: "http://127.0.0.1:8000/api/token/",
          data: this.credentials,
        })
          .then((res) => {
            const user_name = res.config.data.split(",")[0].split(":")[1].split('"')[1]
            this.$store.dispatch('user_Name',user_name)
            localStorage.setItem("jwt", res.data.access);
            // console.log(res)
            // console.log(res.config.data)
            // console.log(res.config.data.split(",")[0].split(":")[1].split('"')[1])
            localStorage.setItem("user_name", res.config.data.split(",")[0].split(":")[1].split('"')[1])
            
            
            this.$emit("login");
            this.$router.push({ name: "home" });
            console.log('로그인 성공!')
          })
          .catch((err) => {
            console.log(err);
          });
      },
    },
  };
  </script>
  