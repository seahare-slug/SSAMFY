<template>
  <div>
    <h5>{{ movie.title }}</h5>
    <p>{{ movie.content }}</p>
  </div>
</template>

<script>
export default {
  name: "RecommendListItem",
  props: {
    movie: Object,
  },
};
</script>

<style></style>
