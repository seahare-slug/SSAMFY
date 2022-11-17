<template>
  <div>
    <h1>님의 프로필</h1>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ProfileView",
  created() {
    axios({
      method: "get",
      url: "http://127.0.0.1:8000/accounts/profile/",
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
