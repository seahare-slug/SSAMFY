<template>
  <div class="wrap-login">
    <h1>Login</h1>
    <div class="wrap-login-form">
      <div>
        <div class="input-form">
          <label for="username">username: </label>
          <input
            type="text"
            id="username"
            v-model="credentials.username"
            placeholder="아이디를 입력해주세요."
            onkeyup="this.value=this.value.replace(/\s/,'')"
          />
        </div>
        <div class="input-form">
          <label for="password">password: </label>
          <input
            type="password"
            id="password"
            v-model="credentials.password"
            @keyup.enter="login"
            placeholder="비밀번호를 입력해주세요."
            onkeyup="this.value=this.value.replace(/\s/,'')"
          />
        </div>
      </div>
      <button class="login-btn" @click="login">Log In</button>
    </div>
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
        })
        .catch((err) => {
          if (
            err.response.data.detail ==
            "No active account found with the given credentials"
          ) {
            alert("유효한 아이디가 아니거나 비밀번호가 틀렸습니다!");
          } else {
            console.log(err);
          }
        });
    },
  },
};
</script>

<style scoped>
.wrap-login {
  position: relative;
}
h1 {
  margin-top: 10%;
}
label {
  color: azure;
  font-size: 24px;
}
input {
  font-size: 18px;
}
.wrap-login {
  height: calc(100vh - 80px);
}
.wrap-login-form {
  display: flex;
  margin: 0 0 0 30%;
  font-weight: bold;
  font-size: 1rem;
  text-align: right;
}
.input-form {
  margin: 10px;
}
.login-btn {
  margin-top: 10px;
  height: 70px;
}
</style>
