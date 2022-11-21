<template>
  <div>
    <div
      v-for="user in users"
      :key="user.id"
    >
      <div v-if="user.username === credentials.username">
        {{ user.username }} 님의 프로필 입니다
        <br>
        {{ user }}
      </div>
    </div>
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
  computed: {
      users() {
        return this.$store.state.users;
      },
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
