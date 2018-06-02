<template>
	<div class="container">
		<canvas id="radar-chart"></canvas>
		<v-layout row wrap>
	      <v-flex xs6>
	        <v-select :items="labels" v-model="course" label="Choisir la matière" single-line @change="actualiser"></v-select>
	      </v-flex>
	    </v-layout>
		<canvas id="line-chart"></canvas>
	</div>
</template>

<script>
  export default {
    data() {
      return {
      	labels: ['Français', 'Allemand', 'Arts Plastiques', 'Anglais', 'Histoire-Géographie', 'Mathématiques', 'Musique', 'Physique-Chimie', 'Science et Vie'],
      	course: "Français"

      }
    },
    mounted() {
    	new Chart(document.getElementById("radar-chart"), {
		    type: 'radar',
		    data: {
		      labels: ['Français', 'Allemand', 'Arts Plastiques', 'Anglais', 'Histoire-Géographie', 'Mathématiques', 'Musique', 'Physique-Chimie', 'Science et Vie'],
		      datasets: [
		        {
		          label: "Elève",
		          fill: true,
		          backgroundColor: "rgba(179,181,198,0.2)",
		          borderColor: "rgba(179,181,198,1)",
		          pointBorderColor: "#fff",
		          pointBackgroundColor: "rgba(179,181,198,1)",
		          data: [0.84, 0.90, 0.8, 0.75, 0.65, 0.51, 0.34, 1, 0.57]
		        }, {
		          label: "Classe",
		          fill: true,
		          backgroundColor: "rgba(255,99,132,0.2)",
		          borderColor: "rgba(255,99,132,1)",
		          pointBorderColor: "#fff",
		          pointBackgroundColor: "rgba(255,99,132,1)",
		          pointBorderColor: "#fff",
		          data: [0.41,0.56,0.68,0.45,0.57,0.78,0.84,0.5,0.68]
		        }
		      ]
		    },
		    options: {
			    scale: {
			        ticks: {
			            beginAtZero: true,
			            min: 0,
			        }
			    },
			    legend: {
			    	labels: {
			    		fontSize: 25
			    	}
			    }
			}
		});
		this.actualiser();
    },
    methods: {
    	actualiser: function(){
    		new Chart(document.getElementById("line-chart"), {
				type: 'line',
				data: {
				labels: ["Semaine 1","Semaine 2","Semaine 3","Semaine 4","Semaine 5"],
				datasets: [{ 
				    data: [0.61, 0.55, 0.49, 0.62, 0.70],
				    label: this.course,
				    borderColor: "#3e95cd",
				    fill: false}]
				},
				options: {}
			});
    	}
    }
  }
</script>

<style>
	.chart {
		size: 50%;
	}
</style>