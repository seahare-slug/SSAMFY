<template>
  <div class="wrap-comment">
    <div>
      <div>{{ comment.username }}</div>
      <div>{{ comment.created_at.slice(0, 10) }}</div>
    </div>
    <div>
      <div class="content">{{ comment.content }}</div>
    </div>
    <span class="delete-btn" @click="deleteComment">🗑</span>
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
      if (this.comment.username === localStorage.getItem("userName")) {
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

<style scoped>
.content {
  padding: 10px;
  background-color: rgba(216, 112, 147, 0.3);
}
.wrap-comment {
  width: 100%;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  border: solid pink 3px;
  padding: 5%;
}
.delete-btn {
  font-size: 36px;
}
</style>
