<template>
  <div>
    <!-- <h1>HomeListItem</h1> -->
    <h5>{{movie.id}}</h5>
    <p>{{movie.title}}</p>
    <p>{{movie.poster_path}}</p>
  </div>
</template>

<script>
export default {
    name: 'HomeListItem',
    props : {
        movie:Object
    }
}
</script>

<style>

</style>