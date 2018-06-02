<template>
  <div class="main">
    <v-card class="questionContainer">
      <v-card-title style="text-align: center">
        <div class="headline">{{ questions.question.text }}</div>
      </v-card-title>
      <v-container class="answersContainer" fluid grid-list-md>
        <v-layout row wrap>
          <v-flex xs32
            v-for="answer in questions.question.answers"
            :key="questions.question.answers.indexOf(answer)"
          >
            <v-btn class="answer" :color="questions.question.colors[questions.question.answers.indexOf(answer)]" @click="changeColor(answer)">
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
      questions: {
        question: {
          id: 0,
          text: "Quel état de la matière est compressible ?",
          answers: ["Gazeux", "Liquide", "Solide", "Superfluide"],
          colors: ["secondary", "secondary", "secondary", "secondary"],
          correct_answer: 0
        }
      },
      valueDeterminate: 70
    };
  },
  methods: {
    changeColor: function(answer) {
      if (
        this.questions.question.answers.indexOf(answer) ===
        this.questions.question.correct_answer
      ) {
        this.questions.question.colors[this.questions.question.correct_answer] =
          "green";
      } else {
        this.questions.question.colors[
          this.questions.question.answers.indexOf(answer)
        ] =
          "red";
      }
      console.log(this.questions.question.colors);
    }
  }
};
</script>

<style>
.questionContainer {
  width: 60vw;
  height: 50vh;
  margin: auto;
  margin-top: 25vh;
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

.progress {
  height: 5vh;
  margin-top: 20vh;
}
</style>
