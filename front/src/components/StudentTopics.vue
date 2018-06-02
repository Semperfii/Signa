<template>
  <div class="main">
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
    <div class="cardContainer">
      <v-card class="topicContainer">
        <v-container fluid grid-list-md>
          <v-layout row wrap>
            <v-flex xs32
              v-for="topic in topics"
              v-bind="{ [`xs${topic.flex}`]: true }"
              :key="topic.id"
            >
              <v-btn class="topic" color="secondary">
                  <div class="headline">{{ topic.title }}</div>
                  <v-spacer></v-spacer>
                  <v-icon>forward</v-icon>
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
  data: () => ({
    topics: [
      { id: 3, title: "Allemand", flex: 6 },
      { id: 0, title: "Anglais", flex: 6 },
      { id: 1, title: "Arts Plastiques", flex: 6 },
      { id: 3, title: "Espagnol", flex: 6 },
      { id: 3, title: "Français", flex: 6 },
      { id: 3, title: "Histoire-Géographie", flex: 6 },
      { id: 2, title: "Mathématiques", flex: 6 },
      { id: 3, title: "Musique", flex: 6 },
      { id: 4, title: "Physique-Chimie", flex: 6 },
      { id: 5, title: "Science et Vie", flex: 6 }
    ],
    dialog: false
  })
};
</script>

<style>
.cardContainer {
  width: 50vw;
  margin: auto;
}

.topicContainer {
  margin-top: 10vh;
}

.topic {
  margin: 1vw;
  display: flex;
  width: 22vw;
  height: 10vh;
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
