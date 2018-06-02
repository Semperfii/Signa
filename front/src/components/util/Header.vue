<template>
  <div class="header">
    <v-toolbar dense flat color="white">
      <v-menu offset-y class="hidden-md-and-up">
        <v-toolbar-side-icon slot="activator"></v-toolbar-side-icon>
        <v-list>
          <v-list-tile>
            <v-list-tile-title>Connecté en tant que {{ name }}</v-list-tile-title>
          </v-list-tile>
          <v-divider></v-divider>
          <v-list-tile color="primary" ripple to="/main/add">
            <v-list-tile-title>Ajouter un match</v-list-tile-title>
          </v-list-tile>
          <v-list-tile v-if="name != null" v-on:click="logout" ripple>
            <v-list-tile-title>Se déconnecter</v-list-tile-title>
          </v-list-tile>
        </v-list>
      </v-menu>
      <v-toolbar-title><a href="#/main"><img src="../../assets/title.png"/></a></v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn flat v-if="name != null" v-on:click="logout">Connecté en tant que {{ name }}</v-btn>
        <v-btn color="primary" to="/main/add">Ajouter un match</v-btn>
      </v-toolbar-items>
    </v-toolbar>
  </div>
</template>

<script>
import auth from "../../modules/auth/index";

export default {
  name: "Header",
  data() {
    return {
      name: null
    };
  },
  methods: {
    logout() {
      auth.logout();
    }
  },
  created() {
    let header = this;

    auth
      .checkAuth()
      .then(() => {
        header.name = auth.user.profile.first_name;
      })
      .catch(err => {
        console.log(err);
      });
  }
};
</script>

<style scoped>
.header {
  margin: 0.5em;
}

@media (min-width: 960px) {
  .header {
    margin: 2em;
  }
}

.toolbar__title,
.toolbar__title a,
.toolbar__title a img {
  height: 100%;
}
</style>
