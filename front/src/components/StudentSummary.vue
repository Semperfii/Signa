<template>
  <div class="main">
    <v-container class="resultsContainer" v-if="answers">
      <v-expansion-panel>
        <v-expansion-panel-content v-for="answer in answers" :key="answers.indexOf(answer)">
          <div slot="header">
            Question {{ answers.indexOf(answer) + 1 }} : {{ answer.question.content }}
            <v-chip color="secondary" v-if="answer.outcome">
              Bonne réponse !
            </v-chip>
            <v-chip color="primary" v-else>
              Mauvais réponse !
            </v-chip>
          </div>
          <v-card>
            <v-card-text>
              Votre réponse était
              <span v-if="answer.outcome"> bonne ! Bravo !</span>
              <span v-else> fausse ! Dommage ! La bonne réponse était {{ answer.question['proposition_' + (answer.question.correct_answer + 1)] }}.</span>
            </v-card-text>
          </v-card>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-container>
  </div>
</template>

<script>
  import axios from 'axios';

  export default {
    data() {
      return {
        answers: null
      }
    },
    mounted() {
      axios.get(process.env.API_URL + '/results').then((results) => {
        this.answers = results.data;
        console.log(this.answers);
      });
    }
  }
</script>

<style>
  .resultsContainer {
    margin: auto;
  }
</style>
