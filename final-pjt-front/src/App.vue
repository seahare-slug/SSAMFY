<template>
  <div id="app">
    <nav>
      <span v-if="isLogined()"> 
        <router-link :to="{ name: 'home' }">Home</router-link> |
        <router-link :to="{ name: 'recommend' }">Recommend</router-link> |
        <router-link :to="{ name: 'ProfileView' }">Profile</router-link> |
        <router-link @click.native="logout" to="#">Logout</router-link>    
      </span>
      <span v-else>
        <router-link :to="{ name: 'home' }">Home</router-link> |
        <router-link :to="{ name: 'recommend' }">Recommend</router-link> |
        <router-link :to="{ name: 'SignUpView' }">SignUpPage</router-link> |
        <router-link :to="{ name: 'LoginView' }">LoginPage</router-link> |
      </span>
    </nav>
    <router-view class="main-container"
    @App-nav="navGet"
    />
  </div>
</template>

<script>

export default {
  name: "App",
  data(){
    return{
      userName : null
    }
  },
  methods: {
    logout() {
      localStorage.removeItem("jwt");
      localStorage.removeItem("userName");
      console.log("로그아웃 됨!");
      this.$router.push({ name: "LoginView" })
    },
    isLogined(){
      this.userName = localStorage.getItem('userName')
      return localStorage.getItem('userName')
    },
    navGet(){
      console.log('nav')
    }
  },
};
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  background-color: pink;
  padding: 30px;
  padding-left: 60%;
}

nav a {
  font-weight: bold;
  color: azure;
}

nav a.router-link-exact-active {
  font-weight: bolder;
  color: black;
}
</style>
