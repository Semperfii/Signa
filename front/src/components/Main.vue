<template>
  <div class="main">
    <v-container grid-list-xl fluid>
      <v-layout column>
        <v-flex xs12 md8 offset-md2>
          <signa-notification v-for="notification in notifications" :key="notification.id" :notification="notification" :snackbar="snackbar"></signa-notification>
        </v-flex>
        <v-flex xs12 md8 offset-md2>
          <v-card class="card--flex-toolbar">
            <v-toolbar card prominent>
              <v-toolbar-title class="headline secondary--text hidden-sm-and-down">Classement général</v-toolbar-title>
              <v-spacer class="hidden-sm-and-down"></v-spacer>
              <v-toolbar-title class="headline grey--text hidden-md-and-up" v-if='!searchDrawer'>Classement</v-toolbar-title>
              <v-spacer class="hidden-md-and-up" v-if='!searchDrawer'></v-spacer>

              <v-text-field v-if='searchDrawer' hide-details single-line label="Recherche" v-model="search" class="search"></v-text-field>
              <v-btn icon @click="searchDrawer = !searchDrawer">
                <v-icon>search</v-icon>
              </v-btn>
              <v-btn icon id="refresh" v-on:click="updateLeaderboard">
                <v-icon>refresh</v-icon>
              </v-btn>
            </v-toolbar>
            <v-divider></v-divider>
            <v-card-text>
              <v-data-table
                :headers="headers"
                :items="users"
                :search="search"
                :rows-per-page-items="rows"
                rows-per-page-text="Joueurs par page :"
                :loading="progress">
                <v-progress-linear slot="progress" color="primary" indeterminate></v-progress-linear>
                <template slot="items" slot-scope="props" v-bind:class="{ me: props.item.id === me_id }">
                  <td v-bind:class="{ me: props.item.id === me_id }" class="text-xs-right">{{ props.item.rank }}</td>
                  <td v-bind:class="{ me: props.item.id === me_id }">{{ props.item.name }}</td>
                  <td v-bind:class="{ me: props.item.id === me_id }" class="text-xs-right">{{ props.item.score }}</td>
                  <td v-bind:class="{ me: props.item.id === me_id }" class="text-xs-right">{{ props.item.matches }}</td>
                  <td v-bind:class="{ me: props.item.id === me_id }" class="text-xs-right">{{ props.item.victories }}</td>
                  <td v-bind:class="{ me: props.item.id === me_id }" class="text-xs-right">{{ props.item.looses }}</td>
                  <td v-bind:class="{ me: props.item.id === me_id }" class="text-xs-right">{{ props.item.goal_average }}</td>
                </template>
                <v-alert slot="no-results" :value="true" color="error" icon="warning">
                  Pas de resultats pour "{{ search }}".
                </v-alert>
              </v-data-table>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>

    <v-snackbar top v-model="snackbar.show">{{ snackbar.text }}<v-btn flat color="pink" @click.native="snackbar.show = false">Close</v-btn>
    </v-snackbar>
  </div>
</template>

<script>
  import auth from '../modules/auth';
  import Notification from './Notification';
  import axios from 'axios';

  export default {
    name: 'Main',
    components: {
      signaNotification: Notification
    },
    data() {
      return {
        headers: [
          {text: '#', align: 'left', value: 'rank'},
          {text: 'Nom', align: 'left', value: 'name'},
          {text: 'Points', value: 'score'},
          {text: 'Matches', value: 'matches'},
          {text: 'Victoires', value: 'victories'},
          {text: 'Looses', value: 'looses'},
          {text: 'GA', value: 'goal_average'}
        ],
        rows: [25,{"text":"All","value":-1}],
        progress: false,
        users: [],
        users_filtered: [],
        me_id: auth.user.profile.id,
        search: '',
        searchDrawer: false,
        notifications: [],
        snackbar: {
          text: '',
          show: false
        }
      }
    },
    created() {
      this.updateLeaderboard();
      this.getNotifications();
    },
    methods: {
      updateLeaderboard() {
        let main = this;

        this.progress = true;
        axios.get(process.env.API_URL + '/users?score=true')
          .then(function (response) {
            main.users = response.data;
            main.users = main.users.map((item, i) => {
              item.rank = i + 1;
              item.name = item.first_name + ' ' + item.last_name;
              return item;
            });
            main.progress = false;
          })
          .catch(function (error) {
            console.log(error);
          });
      },
      getNotifications() {
        let main = this;
        axios.get(process.env.API_URL + '/notifications')
          .then(function (response) {
            main.notifications = response.data;
          })
          .catch(function (error) {
            console.log(error);
          });
      }
    }
  }
</script>

<style scoped>
  .main {
    width: 100%;
  }

  .me {
    background-color: rgba(216, 245, 221, 0.69);
  }

  #refresh:hover {
    -webkit-animation: rotating 1s linear infinite;
    -moz-animation: rotating 1s linear infinite;
    -ms-animation: rotating 1s linear infinite;
    -o-animation: rotating 1s linear infinite;
    animation: rotating 1s linear infinite;
  }

  .search {
    margin-left: 32px;
  }

  @-webkit-keyframes rotating /* Safari and Chrome */
  {
    from {
      -webkit-transform: rotate(0deg);
      -o-transform: rotate(0deg);
      transform: rotate(0deg);
    }
    to {
      -webkit-transform: rotate(360deg);
      -o-transform: rotate(360deg);
      transform: rotate(360deg);
    }
  }

  @keyframes rotating {
    from {
      -ms-transform: rotate(0deg);
      -moz-transform: rotate(0deg);
      -webkit-transform: rotate(0deg);
      -o-transform: rotate(0deg);
      transform: rotate(0deg);
    }
    to {
      -ms-transform: rotate(360deg);
      -moz-transform: rotate(360deg);
      -webkit-transform: rotate(360deg);
      -o-transform: rotate(360deg);
      transform: rotate(360deg);
    }
  }

</style>
