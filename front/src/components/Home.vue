<template>
  <div class="main">
    <v-container>
      <v-layout column>
        <v-flex>
          <v-text-field
            id="username"
            name="username"
            label="Identifiant"
            prepend-icon=
            v-model="username"
          ></v-text-field>
          <v-text-field
            id="password"
            name="password"
            label="Label Text"
            prepend-icon=
          ></v-text-field>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>
