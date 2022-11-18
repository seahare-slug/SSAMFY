<template>
  <div>
    <h1>{{ credentials.username }}님의 프로필</h1>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ProfileView",
  data() {
    return {
      credentials: {
        username: localStorage.getItem("userName"),
      },
    };
  },
  created() {
    axios({
      method: "post",
      url: "http://127.0.0.1:8000/accounts/profile/",
      data: this.credentials,
    })
      .then(() => {
        console.log("프로필 교신성공!");
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style></style>
