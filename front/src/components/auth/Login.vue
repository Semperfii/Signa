<template>
  <div class="login">
    <v-layout row>
      <v-flex xs12 sm6 offset-sm3>
        <img src="../../assets/title.png" id="title">

        <v-card flat id="card">
          <v-card-title primary-title>
            <div class="text">
              <div class="display-2">Bienvenue</div><v-divider></v-divider><br/>
              <p class="grey--text body-2"><b>signa</b> est le site de League de Bière-Pong de CentraleSupéléc, developpé en collaboration avec l'<b>AdR</b>.</p>

              <v-btn block color="primary" v-on:click="login" id="connect">Se connecter</v-btn>

              <div class="display-1">Concept</div><v-divider></v-divider><br/>
              <p class="grey--text body-2">Rentrez chaque match que vous disputez en indiquant votre partenaire et vos adversaires ainsi que le score final.
            Suivant ce score, un nombre de point est attribué à chaque équipe et un classement est determiné en temps réel.
            En cas de litige, une notification est envoyée aux adversaires qui pourront contester le match.</p>
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
    mounted() {
      let login = this;

      auth.checkAuth().then(() => {
        login.$router.replace('/main');
      }).catch(() => {
      });
    },
    methods: {
      login() {
        auth.login(this);
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
    margin: 2em;
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
