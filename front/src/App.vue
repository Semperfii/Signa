<template>
  <div id="app" class="uk-background-default">
    <v-app>
      <bp-header v-if="!$route.path.includes('login')"></bp-header>
      <router-view/>
    </v-app>
  </div>
</template>

<script>
  import BpHeader from '@/components/util/Header';

  export default {
    name: 'App',
    components: {
      bpHeader: BpHeader
    }
  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    background-color: white;
  }
</style>
