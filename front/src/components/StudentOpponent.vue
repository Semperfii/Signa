<template>
  <v-stepper v-model="e1">
    <v-stepper-header>
      <v-stepper-step :complete="e1 > 1" step="1">Opposant</v-stepper-step>
      <v-divider></v-divider>
      <v-stepper-step :complete="e1 > 2" step="2">Matière</v-stepper-step>
      <v-divider></v-divider>
      <v-stepper-step step="3">C'est parti!</v-stepper-step>
    </v-stepper-header>
    <v-stepper-items>
      <v-stepper-content step="1">
        <v-card class="elevation-0" height="73vh">
          <v-layout row>
            <v-flex xs12 sm6 offset-sm3>
              <v-card>
                <v-toolbar color="primary" dark>
                  <v-toolbar-title>Partie Rapide</v-toolbar-title>
                  <v-spacer></v-spacer>
                  <v-toolbar-items>
                    <v-text-field
                    name="input-1-3"
                    label="Trouve un adversaire"
                    prepend-icon="search"
                    ></v-text-field>
                  </v-toolbar-items>
                </v-toolbar>
                <v-list>
                  <v-list-tile v-for="item in items" :key="item.title" avatar @click="e1 = 2">
                    <v-list-tile-action>
                      <v-icon v-if="item.star" color="primary">star</v-icon>
                      <v-icon v-else-if="item.recent" color="primary">restore</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-content>
                      <v-list-tile-title v-text="item.title"></v-list-tile-title>
                    </v-list-tile-content>
                    <v-list-tile-avatar>
                      <v-avatar color="secondary">
                        <v-icon dark>account_circle</v-icon>
                      </v-avatar>
                    </v-list-tile-avatar>
                  </v-list-tile>
                </v-list>
              </v-card>
            </v-flex>
          </v-layout>
        </v-card>
      </v-stepper-content>
      <v-stepper-content step="2">
        <v-card class="elevation-0" height="73vh">
          <v-container fluid grid-list-md class="topicContainer">
            <v-layout row wrap>
              <v-flex xs32
                v-for="topic in topics"
                v-bind="{ [`xs${topic.flex}`]: true }"
                :key="topic.id"
              >
                <v-btn class="topic" color="primary" @click.native="e1 =3">
                    <div class="headline">{{ topic.title }}</div>
                    <v-spacer></v-spacer>
                    <v-icon>forward</v-icon>
                </v-btn>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card>
      </v-stepper-content>
      <v-stepper-content step="3">
        <v-card class="elevation-0" height="73vh"></v-card>
      </v-stepper-content>
    </v-stepper-items>
  </v-stepper>
</template>

<script>
  export default {
    data () {
      return {
        e1: 0,
        topics: [
          { id: 0, title: "Allemand", flex: 6 },
          { id: 1, title: "Anglais", flex: 6 },
          { id: 2, title: "Arts Plastiques", flex: 6 },
          { id: 3, title: "Espagnol", flex: 6 },
          { id: 4, title: "Français", flex: 6 },
          { id: 5, title: "Histoire-Géographie", flex: 6 },
          { id: 6, title: "Mathématiques", flex: 6 },
          { id: 7, title: "Musique", flex: 6 },
          { id: 8, title: "Physique-Chimie", flex: 6 },
          { id: 9, title: "Science et Vie", flex: 6 }
        ],
        items: [
          { star: true, recent: false, title: 'Sacha Dupont' },
          { star: true, recent: false, title: 'Juliette Adam' },
          { star: true, recent: false, title: 'Clara Delahaye' },
          { star: true, recent: false, title: 'Julien Legrand' },
          { star: true, recent: false, title: 'Liam Smith' },
          { star: false, recent: true, title: 'Corine Maillot' },
          { star: false, recent: true, title: 'Alexandre Petit' },
          { star: false, recent: true, title: 'Léonie Mine' },
          { star: false, recent: true, title: 'Adrien Foucault' },
          { star: false, recent: true, title: 'François Martin' }
        ]
      }
    }
  }
</script>

<style>
.topicContainer {
  width: 50vw;
}

.topic {
  display: flex;
  width: 22vw;
  height: 10vh;
  margin-top: 1vh;
  margin-bottom: 2vh;
}

.elevation-0 {
  margin-top: 5vh;
}
</style>
