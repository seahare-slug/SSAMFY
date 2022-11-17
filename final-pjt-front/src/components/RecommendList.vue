<template>
  <div>
    <h1>RecommendList</h1>
    <button
      @click="toggleClassic"
      >
      <span
        v-if="isClassic === false"
      >고전 명작 on
      </span>
      <span
        v-if="isClassic === true"
      >고전 명작 off
      </span>
    </button>
    <button
      @click="toggleIndependent"
      >
      <span
        v-if="isIndependent === false"
      >독립 영화 on
      </span>
      <span
        v-if="isIndependent === true"
      >독립 영화 off
      </span>
    </button>

    <hr>
    <RecommendListItem
      v-for="movie in movies"
      :key="movie.id"
      :movie="movie"
      :isClassic="isClassic"
      :isIndependent="isIndependent"
    />
  </div>
</template>

<script>
import RecommendListItem from './RecommendListItem.vue';

export default {
    name: 'RecommendList',
    data() {
      return {
        isClassic : false,
        isIndependent : false,
      }
    },
    components:{
        RecommendListItem
    },
    computed: {
        movies() {
            return  this.$store.state.movies
        }
    },
    methods: {
      toggleClassic(){
        this.isClassic = !this.isClassic
        console.log(this.isClassic)
      },
      toggleIndependent(){
        this.isIndependent = !this.isIndependent
      }
    },
    created(){
      console.log(this.genres)
    }
}
</script>

<style>

</style>