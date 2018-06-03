<template>
  <div class="main">
    <v-container>
      <v-layout column>
        <v-flex md12>
          <v-card flat id="card" color="transparent">
            <v-card-title primary-title>
              <div class="display-2">Salut Alexis !</div>
            </v-card-title>
            <v-divider></v-divider>
            <v-card-text>
              <v-layout row>
                <v-flex md3>
                  <img src="../assets/mage.png" class="profile_level"/>
                </v-flex>
                <v-flex md9>
                  <span class="level">Mage des Mathématiques - Niveau 23</span>
                  <v-progress-linear v-model="exp" height="10"></v-progress-linear>
                  <v-layout row wrap align-center class="pa-4">
                    <v-flex class="text-xs-center" md3>
                      <div class="title">Meilleures matières</div>
                    </v-flex>
                    <v-flex>
                      <v-layout column align-center>
                        <v-flex>
                          <v-progress-circular :size="100"
                                               :width="15"
                                               :rotate="-90"
                                               :value="93"
                                               color="secondary">
                            93
                          </v-progress-circular>
                        </v-flex>
                        <v-flex>
                          <b>Mathématiques</b>
                        </v-flex>
                      </v-layout>
                    </v-flex>
                    <v-flex>
                      <v-layout column align-center>
                        <v-flex>
                          <v-progress-circular :size="100"
                                               :width="15"
                                               :rotate="-90"
                                               :value="69"
                                               color="primary">
                            69
                          </v-progress-circular>
                        </v-flex>
                        <v-flex>
                          <b>Physique</b>
                        </v-flex>
                      </v-layout>
                    </v-flex>
                    <v-flex>
                      <v-layout column align-center>
                        <v-flex>
                          <v-progress-circular :size="100"
                                               :width="15"
                                               :rotate="-90"
                                               :value="51"
                                               color="primary">
                            51
                          </v-progress-circular>
                        </v-flex>
                        <v-flex>
                          <b>Histoire</b>
                        </v-flex>
                      </v-layout>
                    </v-flex>
                  </v-layout>
                </v-flex>
              </v-layout>
            </v-card-text>
          </v-card>
        </v-flex>
        <v-flex xs12>
          <v-card class="carte" color="secondary" raised id="dungeon">
            <v-parallax src="/static/dungeon.png" height="300">
              <v-container fill-height fluid>
                <v-layout fill-height>
                  <v-flex xs12 align-end flexbox>
                    <span class="display-2 white--text pacifico">
                      <v-icon color="white" size="1em">fa-unlock-alt</v-icon>
                      Quizz dongeon
                    </span>
                    <p class="white--text subtext">Améliore toi et réponds en ligne aux questions proposées par ton
                      professeur !</p>
                    <div class="play-buttons">
                      <v-btn flat color="white">Résultats</v-btn>
                      <v-btn color="primary" to="/student/question/quizz">Je suis prêt !</v-btn>
                    </div>
                  </v-flex>
                </v-layout>
              </v-container>
            </v-parallax>
          </v-card>
        </v-flex>
        <v-flex xs12>
          <v-card class="carte" color="secondary" raised>
            <v-parallax src="/static/village.jpg" height="300">
              <v-container fill-height fluid>
                <v-layout fill-height>
                  <v-flex xs12 align-end flexbox>
                    <span class="display-2 white--text pacifico">Joue contre un pote !</span>
                    <p class="white--text subtext">Choisis une matière et montre à tes amis que tu es meilleur qu'eux
                      !</p>
                    <div class="play-buttons">
                      <v-btn color="primary" to="/student/opponent">A l'attaque !</v-btn>
                    </div>
                  </v-flex>
                </v-layout>
              </v-container>
            </v-parallax>
          </v-card>
        </v-flex>
        <v-flex xs12>
          <v-card class="carte" color="secondary" raised>
            <v-parallax src="/static/night_hill.gif" height="300">
              <v-container fill-height fluid>
                <v-layout fill-height>
                  <v-flex xs12 align-end flexbox>
                    <span class="display-2 white--text pacifico">Joue en solo</span>
                    <p class="white--text subtext">Choisis ta matière et entraine toi sur une série de 10 questions à
                      ton niveau !</p>
                    <div class="play-buttons">
                      <v-btn color="primary" to="/student/topics">C'est parti !</v-btn>
                    </div>
                  </v-flex>
                </v-layout>
              </v-container>
            </v-parallax>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
  import auth from '../modules/auth';

  export default {
    data() {
      return {
        dialog: false,
        exp: auth.user.profile.xp / 1000 * 100
      };
    },
    created() {
      console.log(this.exp);
    }
  };
</script>

<style>
  .carte {
    margin-top: 20px;
  }

  .level {
    font-family: 'Pacifico', serif;
    font-size: 3rem;
    color: #fb9793;
  }

  .pacifico {
    font-family: 'Pacifico', serif;
  }

  .profile_level {
    max-width: 90%;
    margin: auto;
  }

  .title {
    font-weight: lighter;
    margin: auto;
    display: block;
  }

  .subtext {
    margin-top: 2em;
    font-size: 1.2rem;
  }

  .play-buttons {
    position: absolute;
    right: 2em;
    bottom: 2em;
  }
</style>
