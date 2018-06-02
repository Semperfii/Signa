<template>
  <div class="main">
    <v-container>
      <v-layout column>
        <v-flex xs12>
          <v-card class="carte">
            <v-card-title>
              <div>
                <h1>Quizz Hebdomadaire</h1>
                <br>
                <span>Améliore toi et répond en ligne aux questions proposées par ton professeur !</span>
              </div>
            </v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn flat color="primary">Résultats</v-btn>
              <v-btn flat color="primary">Jouer !</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
        <v-flex xs12>
          <v-card raised class="carte">
            <v-card-title>
              <div>
                <h1>Jouer en solo</h1>
                <br>
                <span>Choisis ta matière et entraine toi sur une série de 10 questions à ton niveau !</span>
              </div>
            </v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn flat color="primary">S'entrainer !</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
        <v-flex xs12>
          <v-card  class="carte">
            <v-card-title>
              <div>
                <h1>Joue contre tes amis</h1>
                <br>
                <span>Choisis une matière et montre à tes amis que tu es meilleur qu'eux !</span>
              </div>
            </v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn flat color="primary">Défier un ami !</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
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
.carte {
  margin-top: 20px;
}
</style>
