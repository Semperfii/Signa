<template>
  <div class="main">
    <v-progress-linear class="progress" height="40" v-model="laps"></v-progress-linear>
    <v-card class="questionContainer">
      <v-card-title>
        <div class="headline">{{ question.text }}</div>
      </v-card-title>
      <v-container class="answersContainer" fluid grid-list-md>
        <v-layout row wrap>
          <v-flex xs32 v-for="answer in question.answers" :key="question.answers.indexOf(answer)">
            <v-btn round class="answer" :color="question.colors[question.answers.indexOf(answer)]" @click="changeQuestion(answer)">
                <div class="headline">{{ answer }}</div>
            </v-btn>
          </v-flex>
        </v-layout>
      </v-container>
    </v-card>
    <v-progress-linear class="progress" v-model="valueDeterminate"></v-progress-linear>
  </div>
</template>

<script>
export default {
  data() {
    return {
      question: {
        id: 0,
        text: "Quel état de la matière est compressible ?",
        answers: ["Gazeux", "Liquide", "Solide", "Superfluide"],
        colors: ["secondary", "secondary", "secondary", "secondary"],
        correct_answer: 0
      },
      valueDeterminate: 0,
      laps: 100,
      timer: null
    };
  },
  created(){
    this.timer = setInterval(this.decrement, 50);
  },
  methods: {
    changeQuestion: function(answer) {
      if (
        this.question.answers.indexOf(answer) ===
        this.question.correct_answer
      ) {
        this.$set(this.question.colors, this.question.correct_answer, "green")
      } else {
        this.$set(this.question.colors, this.question.answers.indexOf(answer), "red");
        this.$set(this.question.colors, this.question.correct_answer, "green");
      };
      this.valueDeterminate+=10;
      clearInterval(this.timer);
    },
    decrement: function() {
      this.laps-=1/3;
      if (this.laps<0) {
        clearInterval(this.timer);
        this.$set(this.question.colors, this.question.correct_answer, "green")
      }
    }
  }
};
</script>

<style>
.questionContainer {
  width: 60vw;
  height: 50vh;
  margin: auto;
  margin-top: 15vh;
  margin-bottom: 15vh;
}

.answerContainer {
  margin: auto;
  display: flex;
  justify-content: space-around;
}

.answer {
  width: 27vw;
  height: 20vh;
}

</style>
