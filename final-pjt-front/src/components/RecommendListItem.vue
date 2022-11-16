<template>
  <div>
    <!-- <h1>RecommendListItem</h1> -->
    <h5>{{movie.title}}</h5>
    <p>{{movie.content}}</p>
  </div>
</template>

<script>
export default {
    name: 'RecommendListItem',
    props : {
        movie:Object
    }
}
</script>

<style>

</style>