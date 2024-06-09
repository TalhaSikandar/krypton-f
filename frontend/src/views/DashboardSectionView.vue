<template>
  <div class="section">
    <h1 class="title">Hello,&nbsp; <strong>{{ company_name }}!</strong><br>Welcome to Krypton!</h1>
    <p class="home-dash-para">This is where you can view key metrics, reports, and other relevant information for your company.</p>
    <div class="charts-container">
      <div class="card">
        <button @click="toggleChart" class="toggle-button">{{ showAllStores ? 'Show Top Stores' : 'Show All Stores' }}</button>
        <Bar
          id="line-chart"
          :options="chartOptions"
          :data="chartData"
        />
        <p class="card-title" style="color: var(--white-background-color); padding-left: 2rem;">Stores Performance</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import store from '@/store'; // import your Vuex store
import { mapState } from 'vuex';
import { Bar } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);

export default {
  computed: {
    ...mapState(['company_name']),
  },
  components: {
    Bar,
  },
  mounted() {
    this.getStores();
    document.title = 'Home | Krypton';
  },
  data() {
    return {
      stores: [],
      showAllStores: false,
      chartData: {
        labels: [],
        datasets: [],
      },
      chartOptions: {
        responsive: true,
      },
    };
  },
  methods: {
    generateRandomColors(count) {
      const colors = [];
      for (let i = 0; i < count; i++) {
        const randomColor = `rgba(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, 0.8)`;
        colors.push(randomColor);
      }
      return colors;
    },
    getStores() {
      axios
        .get('dashboard/stores/products/', {
          headers: {
            Authorization: `Bearer ${store.state.token}`,
          },
        })
        .then(response => {
          this.stores = response.data;
          this.updateChartData();
        })
        .catch(error => {
          console.error('Error fetching stores:', error);
        });
    },
    updateChartData() {
      const storesToDisplay = this.showAllStores ? this.stores : this.stores.slice(0, 5); // Show top 5 stores by default
      const labels = storesToDisplay.map(store => String(store.store));
      const data = storesToDisplay.map(store => store.sold_amount);
      const backgroundColors = this.generateRandomColors(storesToDisplay.length);

      this.chartData = {
        labels: labels,
        datasets: [{
          label: 'Sold Amount',
          data: data,
          backgroundColor: backgroundColors,
        }],
      };
    },
    toggleChart() {
      this.showAllStores = !this.showAllStores;
      this.updateChartData();
    },
  },
};
</script>

<style scoped>
.card {
  background-color: var(--menu-background-color);
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
  width: 500px;
  height: 300px;
  position: relative;
}

.home-dash-para {
  color: var(--white-background-color);
}

.charts-container {
  display: flex;
  gap: 2rem;
  flex-wrap: wrap;
}

.toggle-button {
  position: absolute;
  top: 10px;
  right: 10px;
  padding: 5px 10px;
  background-color: var(--button-background-color);
  color: var(--button-text-color);
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.card-title {
  color: var(--white-background-color);
  padding-left: 2rem;
}
</style>
