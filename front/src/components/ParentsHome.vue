<template>
  <div class="main">
    <v-toolbar class="toolbar">
      <v-toolbar-title>NOM Prénom</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down">
      <v-spacer></v-spacer>
        <v-layout wrap justify-space-around align-center>
          <span style="margin-right: 2vw">Espace Parents</span>
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
  </div>
</template>
