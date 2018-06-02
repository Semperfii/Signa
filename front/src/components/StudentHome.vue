<template>
  <div class="main">
<<<<<<< HEAD
=======
    <v-toolbar class="toolbar">
      <v-toolbar-title>NOM Prénom</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down">
      <v-spacer></v-spacer>
        <v-layout wrap justify-space-around align-center>
          <v-btn icon @click="dialog = true">
            <v-avatar color="indigo">
              <v-icon dark style="margin-left: 0">account_circle</v-icon>
            </v-avatar>
          </v-btn>
          <v-dialog v-model="dialog">
            <v-card class="dialog">
              <v-card-actions>
                <v-btn color="secondary">
                  <span>Modifier le profil</span>
                  <v-icon>create</v-icon>
                </v-btn>
                <v-btn color="primary">
                  <span>Se déconnecter</span>
                  <v-icon>exit_to_app</v-icon>
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-layout>
      </v-toolbar-items>
    </v-toolbar>
>>>>>>> teacher_dashboard
    <div class="cardContainer">
      <v-card class="cards">
        <v-container
          fluid
          style="min-height: 0;"
          grid-list-lg
        >
          <v-layout row wrap>
            <v-flex xs12>
              <v-btn color="secondary" class="white--text">
                <div class="headline">Ouverture du quizz hebdomadaire:<br>*countdown*</div>
              </v-btn>
            </v-flex>
            <v-flex xs12>
              <v-btn color="secondary" class="white--text">
                <div class="headline">Entraîne toi en solo</div>
              </v-btn>
            </v-flex>
            <v-flex xs12>
              <v-btn color="secondary" class="white--text">
                <div class="headline">Défie tes amis</div>
              </v-btn>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dialog: false
    };
  }
};
</script>

<style>
.cards {
  margin-top: 10vh;
}

.cardContainer {
  width: 50vw;
  margin: auto;
}

.white--text {
  width: 48vw;
  height: 20vh;
}

.dialog {
  display: flex;
  justify-content: space-around;
  width: 28vw;
}

.icon {
  margin-left: 1vw;
}
</style>
