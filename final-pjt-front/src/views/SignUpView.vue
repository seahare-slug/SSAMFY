<template>
  <div class="wrap-signup">
    <h1>Sign up</h1>
    <form class="wrap-signup-form" @submit.prevent="signUp">
      <div>
        <div class="input-form">
          <label for="username">username : </label>
          <input
            type="text"
            id="username"
            v-model="credentials.username"
            placeholder="아이디를 입력해주세요."
            onkeyup="this.value=this.value.replace(/\s/,'')"
          />
        </div>
        <div class="input-form">
          <label for="password">password : </label>
          <input
            type="password"
            id="password"
            v-model="credentials.password"
            placeholder="비밀번호를 입력해주세요."
            onkeyup="this.value=this.value.replace(/\s/,'')"
          />
        </div>
        <div class="input-form">
          <label for="passwordConfirmation">password confirmation : </label>
          <input
            class="re-type-pw"
            type="password"
            id="passwordConfirmation"
            v-model="credentials.passwordConfirmation"
            placeholder="비밀번호를 다시 입력해주세요."
            onkeyup="this.value=this.value.replace(/\s/,'')"
          />
        </div>
      </div>
      <button class="signup-btn">Sign Up</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SignupView",
  data() {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
      },
    };
  },
  methods: {
    signUp() {
      if (this.credentials.username.length < 4) {
        alert("아이디는 4글자 이상 입력해주세요.");
        return;
      } else if (this.credentials.password.length < 4) {
        alert("비밀번호는 4글자 이상 입력해주세요.");
        return;
      } else if (
        this.credentials.password != this.credentials.passwordConfirmation
      ) {
        alert("원래 입력하신 비밀번호와 다릅니다.");
      } else {
        axios({
          method: "post",
          url: "http://127.0.0.1:8000/accounts/signup/",
          data: this.credentials,
        })
          .then(() => {
            this.$router.push({ name: "LoginView" });
          })
          .catch((err) => {
            if (
              err.response.data.username ==
              "A user with that username already exists."
            ) {
              alert(
                "이미 존재하는 username 입니다! 다른 username을 사용해 주세요. "
              );
            } else {
              console.log(err);
            }
          });
      }
    },
  },
};
</script>

<style scoped>
h1 {
  margin-top: 10%;
}
label {
  color: azure;
  font-size: 24px;
}
.wrap-signup {
  height: calc(100vh - 80px);
}
input {
  font-size: 18px;
}
.wrap-signup-form {
  display: flex;
  margin: 0 0 0 20%;
  font-weight: bold;
  font-size: 1rem;
  text-align: right;
}
.input-form {
  margin: 10px;
}
.signup-btn {
  margin-top: 10px;
  height: 110px;
}
</style>
