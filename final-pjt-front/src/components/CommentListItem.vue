<template>
  <div>
    <h3>Here is Comment items</h3>
    <div>{{ comment.content }}</div>
    <div>{{ comment.username }}</div>
    <div>{{ comment.created_at }}</div>
    <button @click="deleteComment">[ DELETE ]</button>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";
export default {
  name: "CommentListItem",
  props: {
    comment: Object,
  },
  methods: {
    deleteComment() {
      if (this.comment.username === localStorage.getItem("userName")){

        axios({
          method: "delete",
          url: `${API_URL}/api/v1/movies/${this.comment.id}/comment/delete/`,
        })
        .then(() => {
          this.getComments();
        })
        .catch((err) => {
          console.log(err);
        });
      }
    },
    getComments() {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/${this.$route.params.id}/comment/`,
      })
        .then((res) => {
          this.comments = res.data;
          this.$store.dispatch("getComments", this.comments);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style></style>
