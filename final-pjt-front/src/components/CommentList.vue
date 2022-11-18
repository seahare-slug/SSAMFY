<template>
  <div>
    <h1>THIS IS CONTETNLIST</h1>
    <CommentListItem
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
    />
  </div>
</template>

<script>
import CommentListItem from "@/components/CommentListItem.vue";

export default {
  name: "CommentList",
  components: {
    CommentListItem,
  },
  computed: {
    comments() {
      return this.$store.state.comments;
    },
  },
};
</script>

<style></style>
