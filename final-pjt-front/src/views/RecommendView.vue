<template>
  <div>
    <h1>Recommend</h1>
    <hr>
    <RecommendList/>
  </div>
</template>

<script>
import RecommendList from '../components/RecommendList.vue'

export default {
    name : 'RecommendView',
    components: {
        RecommendList,
    }
}
</script>

<style>

</style>