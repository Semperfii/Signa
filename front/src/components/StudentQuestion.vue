<template>
  <div class="main">
    <v-progress-linear class="progress" height="40" v-model="laps"></v-progress-linear>
    <v-container>
      <v-layout column wrap>
        <v-flex sm12>
          <v-card class="questionContainer" v-if="question">
            <v-card-title>
              <div class="headline">{{ question.content }}</div>
            </v-card-title>
            <v-container class="propositionsContainer" grid-list-md>
              <v-layout row wrap>
                <v-flex xs6 v-for="answer in question.propositions" :key="question.propositions.indexOf(answer)"
                        align-center>
                  <v-btn round class="answer" :color="question.colors[question.propositions.indexOf(answer)]"
                         @click="changeQuestion(answer)">
                    <div class="answer-text">{{ answer }}</div>
                  </v-btn>
                </v-flex>
              </v-layout>
            </v-container>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
    <v-progress-linear class="progress bottom-progress" v-model="valueDeterminate"></v-progress-linear>

    <v-snackbar
      :timeout="3000"
      bottom
      v-model="snackbar.active">
      {{ snackbar.text }}
      <v-btn flat color="pink" @click.native="snackbar.active = false">Close</v-btn>
    </v-snackbar>
    <v-snackbar
      :timeout="3000"
      top
      v-model="snackbardev.active">
      {{ snackbardev.text }}
      <v-btn flat color="pink" @click.native="snackbardev.active = false">Close</v-btn>
    </v-snackbar>
  </div>
</template>

<script>
  import axios from 'axios';

  export default {
    data() {
      return {
        question: null,
        question_id: 0,
        valueDeterminate: 0,
        laps: 100,
        timer: null,
        mode: null,
        snackbar: {
          active: false,
          text: ""
        },
        snackbardev: {
          active: false,
          text: ""
        }
      };
    },
    created() {
      this.mode = this.$route.params.type;

      this.loadQuestion();
    },
    methods: {
      changeQuestion: function (answer) {
        let outcome = false;
        if (this.question.propositions.indexOf(answer) === this.question.correct_answer) {
          this.$set(this.question.colors, this.question.correct_answer, "green");
          outcome = true;
          this.snackbar.text = "Bonne réponse !";
        } else {
          this.$set(this.question.colors, this.question.propositions.indexOf(answer), "red");
          this.$set(this.question.colors, this.question.correct_answer, "green");
          this.snackbar.text = "Mauvaise réponse !";
        }
        this.snackbar.active = true;
        this.valueDeterminate += 10;
        this.question_id += 1;
        clearInterval(this.timer);

        axios.post(process.env.API_URL + "/results", {
          question_id: this.question.id,
          outcome: outcome
        }).then((result) => {
          setTimeout(this.loadQuestion, 2000);
          this.snackbardev.text = " Score : " + (result.data.score);
        });
      },
      decrement: function () {
        this.laps -= 1 / 3;
        if (this.laps < 0) {
          clearInterval(this.timer);
          this.$set(this.question.colors, this.question.correct_answer, "green");
          this.changeQuestion(null);
        }
      },
      loadQuestion() {
        this.question = null;
        this.laps = 100;
        this.timer = null;
        if (this.question_id !== 10) {
          axios.get(process.env.API_URL + "/questions/" + this.question_id).then((result) => {
            this.question = result.data;
            this.snackbardev.text += " Difficultée : " + result.data.difficulty;
            this.snackbardev.active = true;
            this.question.colors = ["secondary", "secondary", "secondary", "secondary"];
            this.timer = setInterval(this.decrement, 50);
          });
        } else {
          this.$router.replace('/student/summary');
        }
      }
    }
  };
</script>

<style>
  .main {
    min-height: 100vh;
  }

  .headline {
    font-family: 'Pacifico', serif;
  }

  .answer-text {
    font-weight: 200;
    font-size: 2rem;
    color: white;
  }

  .answer {
    height: 200px;
    width: 400px;
    margin: 2em auto;
    display: block;
  }

  .bottom-progress {
    position: fixed;
    bottom: 0;
    left: 0;
  }

</style>
