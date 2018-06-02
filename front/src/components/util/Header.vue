<template>
  <div class="header">
    <v-toolbar dense flat color="white">
      <v-toolbar-title><a href="#/main"><img src="../../assets/title.png"/></a></v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-menu v-model="menu" offset-y>
          <v-avatar slot="activator">
            <img src="https://randomuser.me/api/portraits/men/55.jpg"/>
          </v-avatar>
          <v-card>
            <v-list>
              <v-list-tile avatar>
                <v-list-tile-avatar>
                  <img src="https://randomuser.me/api/portraits/men/55.jpg"/>
                </v-list-tile-avatar>
                <v-list-tile-content>
                  <v-list-tile-title>{{ name }}</v-list-tile-title>
                  <v-list-tile-sub-title>6ème A - Collège Juliette Adam</v-list-tile-sub-title>
                </v-list-tile-content>
              </v-list-tile>
            </v-list>
            <v-divider></v-divider>
            <v-list>
              <v-list-tile avatar @click="">
                <v-list-tile-action>
                  <v-icon color="primary">fa-chart-bar</v-icon>
                </v-list-tile-action>
                <v-list-tile-title>Résultat</v-list-tile-title>
              </v-list-tile>
              <v-list-tile avatar @click="">
                <v-list-tile-action>
                  <v-icon color="primary">fa-trophy</v-icon>
                </v-list-tile-action>
                <v-list-tile-title>Trophées</v-list-tile-title>
              </v-list-tile>
            </v-list>
            <v-divider></v-divider>
            <v-list>
              <v-list-tile @click="logout">
                <v-list-tile-title>
                  Se déconnecter
                </v-list-tile-title>
              </v-list-tile>
            </v-list>
          </v-card>
        </v-menu>
      </v-toolbar-items>
    </v-toolbar>
  </div>
</template>

<script>
import auth from "../../modules/auth/index";

  export default {
    name: 'Header',
    data() {
      return {
        name: null,
        menu: false
      }
    },
    methods: {
      logout() {
        auth.logout();
      }
    },
    created() {
      let header = this;

      auth.checkAuth().then(() => {
        header.name = auth.user.profile.first_name + " " + auth.user.profile.last_name;
      }).catch((err) => {
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
