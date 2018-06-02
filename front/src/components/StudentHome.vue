<template>
  <div class="main">
    <v-toolbar class="toolbar">
      <v-toolbar-title>NOM Prénom</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down">
      <v-spacer></v-spacer>
      <v-layout wrap justify-space-around align-center>
        <v-avatar color="indigo">
          <v-icon dark>account_circle</v-icon>
        </v-avatar>
      </v-layout>
      </v-toolbar-items>
    </v-toolbar>
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
</style>
