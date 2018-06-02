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

    <v-container fluid grid-list-xl text-xs-center>
        <v-expansion-panel >
            <v-layout>
                <v-flex xs12>
                    <v-expansion-panel-content v-for="semaine in semaines" :key="semaine.name">
                    <div slot="header">{{semaine.title}} </div>
                        <v-btn color="info" v-on:click="reset(semaine)">Reset : Semaine précédente</v-btn>    
                        <v-data-table
                            v-model="semaine.checked"
                            :headers="headers"
                            :items="quiz"
                            :pagination.sync="pagination"
                            select-all
                            item-key="name"
                            class="elevation-1"
                        >
                            <template slot="headers" slot-scope="props">
                            <tr>
                                <th>
                                <v-checkbox
                                    :input-value="props.all"
                                    :indeterminate="props.indeterminate"
                                    primary
                                    hide-details
                                    @click.native="toggleAll"
                                ></v-checkbox>
                                </th>
                                <th
                                v-for="header in props.headers"
                                :key="header.text"
                                :class="['column sortable', pagination.descending ? 'desc' : 'asc', header.value === pagination.sortBy ? 'active' : '']"
                                @click="changeSort(header.value)"
                                >
                                <v-icon small>arrow_upward</v-icon>
                                {{ header.text }}
                                </th>
                            </tr>
                            </template>
                            <template slot="items" slot-scope="props">
                            <tr :active="props.selected" @click="props.selected = !props.selected">
                                <td>
                                <v-checkbox
                                    :input-value="props.selected"
                                    primary
                                    hide-details
                                ></v-checkbox>
                                </td>
                                <td>{{ props.item.name }}</td>
                                <td class="text-xs-center">{{ props.item.questions }}</td>
                                <td class="text-xs-center">{{ props.item.difficulty }}</td>
                                <td class="text-xs-center">{{ props.item.success }}</td>
                            </tr>
                            </template>
                        </v-data-table>
                    </v-expansion-panel-content>
                </v-flex>
            </v-layout>
        </v-expansion-panel>
    </v-container>

  </div>
</template>

<script>
export default {
  data() {
    return {
        items: [
          { title: 'Accueil', icon: 'dashboard' },
          { title: 'Quiz', icon: 'question_answer' },
          { title: 'Données', icon: 'data_usage'}
        ],
        semaines : [
            { title : 'Semaine 1', texte: 'Lol t nul', switch: false},
            { title : 'Semaine 2', texte: 'Lol t nul', switch: false},
            { title : 'Semaine 3', texte: 'Lol t nul', switch: false},
            { title : 'Semaine 4', texte: 'Lol t nul', switch: false},
            { title : 'Semaine 5', texte: 'Lol t nul', switch: false}
        ],
        right: null,
        dialog: false,
        pagination: { sortBy: 'questions' },
        headers: [
            { text: 'Quiz', align: 'left', value: 'name'},
            { text: 'Nombre de questions', value: 'questions' },
            { text: 'Difficulté', value: 'difficulty' },
            { text: 'Réussite', value: 'success' }
        ],
        quiz: [
            { value : false, name :'Calcul - Fractions', questions : 18, difficulty: 'Facile', success: '82%' },
            { value : false, name :'Calcul - Thalès 1', questions : 10, difficulty: 'Facile', success: '78%' },
            { value : false, name :'Calcul - Thalès 2', questions : 20, difficulty: 'Difficile', success: '23%' },
            { value : false, name :'Géométrie - Quadrilatères', questions : 15, difficulty: 'Difficile', success: '32%' },
            { value : false, name :'Géométrie - Cercles', questions : 15, difficulty: 'Moyen', success: '52%' },
            { value : false, name :'Calcul - Division', questions : 16, difficulty: 'Facile', success: '90%' },
        ]
    };
  },
  methods: {
      toggleAll () {
        if (this.selected.length) this.selected = []
        else this.selected = this.desserts.slice()
      },
      changeSort (column) {
        if (this.pagination.sortBy === column) {
          this.pagination.descending = !this.pagination.descending
        } else {
          this.pagination.sortBy = column
          this.pagination.descending = false
        }
      },
      reset : function (semaine) {
        if (this.semaines.indexOf(semaine) > 0)  {
            semaine.checked = [];
            this.semaines[this.semaines.indexOf(semaine)-1].checked.forEach((element) => {
                semaine.checked.push(element);
            }, this);
        }
      }
  }
};
</script>

<style>

</style>
