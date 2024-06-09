<template>
      <div class="section">
         <h1 class="title">Hello,&nbsp; <strong>{{company_name}}!</strong><br>Welcome to Krypton!</h1>
         <p class="home-dash-para">This is where you can view key metrics, reports, and other relevant information for your company.</p>
    <div class="charts-container">
    <div class="card">
      <Pie
        id="my-chart-id"
        :options="chartOptions"
        :data="chartData"
      />
          </div>
    <div class="card">
      <Bar
        id="my-chart-id"
        :options="chartOptions"
        :data="chartData"
      />
          </div>
    <div class="card">
      <Line
        id="my-chart-id"
        :options="chartOptions"
        :data="chartData"
      />
          </div></div>
        </div>
</template>


<script>
import axios from 'axios'
import { mapState }from 'vuex';
import { Pie , Bar, Line} from 'vue-chartjs'
import { Chart as ChartJS, Title, PointElement, LineElement, Tooltip, ArcElement, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, PointElement, Tooltip, ArcElement, LineElement,  Legend, BarElement, CategoryScale, LinearScale)
export default {
  computed: {
    ...mapState(['company_name']),
  },
  components: {
    Pie,
    Bar,
    Line
  },
data() {
    return {
      chartData: {
        labels: [ 'January', 'February', 'March' ],
        datasets: [ 
          { data: [40, 20, 12] ,
      backgroundColor: ['#0a152f', '#9d4edd', '#00D8FF', '#DD1B16'],
          },
        ]
      },
      chartOptions: {
        responsive: true
      }
    }
  }
};
</script>

<style scoped>
.card {
  background-color: var(--white-background-color);
  border-radius: 10px; /* Adjust the radius for rounded corners */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px; /* Adjust spacing between cards */
  width: 500px; /* Adjust width of the card */
  height: 300px; /* Adjust height of the card */
}
.home-dash-para {
  color: var(--white-background-color);
}

.charts-container {
  display: flex;
  gap: 2rem;
  flex-wrap: wrap; /* Allow content to wrap */
}
</style>

