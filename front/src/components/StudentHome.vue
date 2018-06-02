<template>
  <div class="main">
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
