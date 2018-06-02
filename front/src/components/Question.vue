<template>
  <div>
    <v-container>
      <h1>{{question.text}}</h1>
      <v-radio-group v-model="radios" :mandatory="true">
        <v-radio :label="question.choix1" value="choix1"></v-radio>
        <v-radio :label="question.choix2" value="choix2"></v-radio>
        <v-radio :label="question.choix3" value="choix3"></v-radio>
        <v-radio :label="question.choix4" value="choix4"></v-radio>
      </v-radio-group>
      <v-btn color="primary" @click="verify(radios, question) ">Répondre</v-btn>
      <h1>{{correct}}</h1>
    </v-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      question: {
        text: "Quel est le nom du premier primate à se déplacer debout ?",
        choix1: "Australopithèque",
        choix2: "Homo Sapiens",
        choix3: "Homo Erectus",
        choix4 : "Homo Abilis",
        answer: "choix1"
      },
      radios: "",
      correct: false
    }
  },
  methods: {
    verify: function(radios, question){
      this.correct = radios == question.answer;
    }
  }
}
</script>