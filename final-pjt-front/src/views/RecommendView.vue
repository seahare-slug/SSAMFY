<template>
  <div class="wrap-recommand">
    <h1>Recommend</h1>
    <hr />
    <RecommendList />
  </div>
</template>

<script>
import RecommendList from "../components/RecommendList.vue";

export default {
  name: "RecommendView",
  components: {
    RecommendList,
  },
};
</script>

<style scoped>
.wrap-recommand {
  height: calc(100vh - 80px);
}
</style>
