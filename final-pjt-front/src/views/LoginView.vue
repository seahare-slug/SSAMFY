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
  data() {
    return {
      credentials: {
        username: null,
        password: null,
      },
    };
  },
  methods: {
    login() {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/token/",
        data: this.credentials,
      })
        .then((res) => {
          const userName = res.config.data
            .split(",")[0]
            .split(":")[1]
            .split('"')[1];
          this.$store.dispatch("userName", userName);
          localStorage.setItem("jwt", res.data.access);
          localStorage.setItem("userName", userName);

          this.$emit("login");
          this.$router.push({ name: "home" });
          console.log("로그인 성공!");
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>
