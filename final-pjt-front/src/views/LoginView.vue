<template>
  <div>
    <h1>Login</h1>
    <div>
      <label for="username">사용자 이름: </label>
      <input type="text" id="username" v-model="credentials.username"
      placeholder="아이디를 입력해주세요."
      onkeyup="this.value=this.value.replace(/\s/,'')"
      />
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input
        type="password"
        id="password"
        v-model="credentials.password"
        @keyup.enter="login"
        placeholder="비밀번호를 입력해주세요."
        onkeyup="this.value=this.value.replace(/\s/,'')"
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
        })
        .catch((err) => {
          if (err.response.data.detail == 'No active account found with the given credentials') {
              alert('아이디가 없습니다! 회원가입을 진행해 주세요. ')
            }
          else {
              console.log(err)
            }
        });
    },
  },
};
</script>
