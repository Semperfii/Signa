<template>
  <div class="main">
    <v-container class="resultsContainer">
      <v-expansion-panel>
        <v-expansion-panel-content v-for="question in questions" :key="questions.indexOf(question)">
          <div slot="header">{{ `Question ${questions.indexOf(question)}` }}</div>
          <v-card>
            <v-card-text>{{ question.help }}</v-card-text>
          </v-card>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-container>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        questions: [
          {
            id: 0,
            text: "Quel état de la matière est compressible ?",
            answers: ["Gazeux", "Liquide", "Solide", "Superfluide"],
            colors: ["secondary", "secondary", "secondary", "secondary"],
            correct_answer: 0,
            help: "blablabla"
          },
          {
            id: 1,
            text: "Quel état de la matière est compressible ?",
            answers: ["Gazeux", "Liquide", "Solide", "Superfluide"],
            colors: ["secondary", "secondary", "secondary", "secondary"],
            correct_answer: 0,
            help: "blablabla bis"
          },
          {
            id: 2,
            text: "Quel état de la matière est compressible ?",
            answers: ["Gazeux", "Liquide", "Solide", "Superfluide"],
            colors: ["secondary", "secondary", "secondary", "secondary"],
            correct_answer: 0,
            help: "blablabla ter"
          }
        ]
      }
    }
  }
</script>

<style>
.resultsContainer {
  margin: auto;
}
</style>
