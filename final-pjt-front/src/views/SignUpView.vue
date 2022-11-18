<template>
  <div>
    <h1>Sign up</h1>
    <form @submit.prevent="signUp">
      <label for="username">username</label>
      <input type="text" id="username" v-model="credentials.username" />
      <br />
      <label for="password">password : </label>
      <input type="text" id="password" v-model="credentials.password" />
      <br />
      <label for="passwordConfirmation">password confirmation : </label>
      <input
        type="text"
        id="passwordConfirmation"
        v-model="credentials.passwordConfirmation"
      />
      <input type="submit" value="Signup" />
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
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/accounts/signup/",
        data: this.credentials,
      })
        .then(() => {
          this.$router.push({ name: "LoginView" });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style></style>
