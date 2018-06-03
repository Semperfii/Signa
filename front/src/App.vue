<template>
  <div id="app" class="uk-background-default">
    <v-app>
      <bp-header v-if="forbiddenPath()"></bp-header>
      <transition name="fade" mode="out-in">
        <router-view></router-view>
      </transition>
    </v-app>
  </div>
</template>

<script>
  import BpHeader from '@/components/util/Header';

  export default {
    name: 'App',
    components: {
      bpHeader: BpHeader
    },
    methods: {
      forbiddenPath: function() {
        if ((this.$route.name === 'Login') || (this.$route.name === 'StudentQuestion')) {
          return false;
        }
        return true;
      }
    }
  }
</script>

<style>
  #app {
    font-family: 'Roboto', Helvetica, Arial, sans-serif;
    color: #232323;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    background: white url('./assets/background.png');
    min-height: 100vh;
  }

  .fade-enter-active, .fade-leave-active {
    transition: opacity .5s;
  }

  .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
    opacity: 0;
  }
</style>
