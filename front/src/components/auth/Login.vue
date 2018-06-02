<template>
  <div class="login">
    <v-layout row>
      <v-flex xs12 sm6 offset-sm3>
        <img src="../../assets/title.png" id="title">

        <v-card flat id="card" color="transparent">
          <v-card-title primary-title>
            <div class="text">
              <v-text-field name="email" label="Email" v-model="email"></v-text-field>
              <v-text-field name="password" type="password" label="Mot de passe" v-model="password"></v-text-field>
              <v-btn block color="primary" v-on:click="login" id="connect">Se connecter</v-btn>
            </div>
          </v-card-title>
        </v-card>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
  import auth from "../../modules/auth/index";

  export default {
    name: 'Login',
    data() {
      return {
        email: "",
        password: ""
      }
    },
    mounted() {
      let login = this;

      auth.checkAuth().then(() => {
        login.$router.replace('/main');
      }).catch(() => {
      });
    },
    methods: {
      login() {
        auth.login(this, this.email, this.password);
      }
    }
  }
</script>

<style scoped>
  .login {
    width: 100%;
    text-align: center;
  }

  #title {
    width: 600px;
    max-width: 90%;
    margin-top: 3em;
  }

  #card {
    margin: 4em;
  }

  .text {
    width: 500px;
    max-width: 90%;
    margin: auto;
    text-align: left;
  }

  #connect {
    margin-top: 2em;
    margin-bottom: 2em;
  }
</style>
