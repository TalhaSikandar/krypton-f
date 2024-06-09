<template>
  <div class="section">
    <h1 class="title">Hello,&nbsp; <strong>{{ company_name }}!</strong><br>Welcome to Krypton!</h1>
    <p class="home-dash-para">This is where you can view key metrics, reports, and other relevant information for your company.</p>
    <div class="charts-container">
      <div class="card">
        <button @click="toggleShowAll('stores')" class="toggle-button">{{ showAllStores ? 'Show Top Stores' : 'Show All Stores' }}</button>
        <Bar
          id="store-chart"
          :options="storeChartOptions"
          :data="storeChartData"
        />
       <p class="card-title" style="color: var(--white-background-color); padding-left: 2rem;">Stores Performance</p>
      </div>
      <div class="card">
        <button @click="toggleShowAll('warehouses')" class="toggle-button">{{ showAllWarehouses ? 'Show Top Warehouses' : 'Show All Warehouses' }}</button>
        <Bar
          id="warehouse-chart"
          :options="warehouseChartOptions"
          :data="warehouseChartData"
        />
       <p class="card-title" style="color: var(--white-background-color); padding-left: 2rem;">Warehouses Index</p>
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
    this.getWarehouses();
    document.title = 'Home | Krypton';
  },
  data() {
    return {
      stores: [],
      warehouses: [],
      showAllStores: false,
      showAllWarehouses: false,
      storeChartData: {
        labels: [],
        datasets: [],
      },
      warehouseChartData: {
        labels: [],
        datasets: [],
      },
      storeChartOptions: {
        responsive: true,
      },
      warehouseChartOptions: {
        responsive: true,
      },
      chartType: 'stores', // Default chart type to display
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
          this.updateStoreChartData();
        })
        .catch(error => {
          console.error('Error fetching stores:', error);
        });
    },
    getWarehouses() {
      axios
        .get('dashboard/warehouses/products/', {
          headers: {
            Authorization: `Bearer ${store.state.token}`,
          },
        })
        .then(response => {
          this.warehouses = response.data;
          console.log(this.warehouses, "warehouse");
          this.updateWarehouseChartData();
        })
        .catch(error => {
          console.error('Error fetching warehouses:', error);
        });
    },
    updateStoreChartData() {
      const storesToDisplay = this.showAllStores ? this.stores : this.stores.slice(0, 4); // Show top 4 stores or all stores
      const labels = storesToDisplay.map(store => String(store.store));
      const data = storesToDisplay.map(store => store.sold_amount);
      const backgroundColors = this.generateRandomColors(storesToDisplay.length);

      this.storeChartData = {
        labels: labels,
        datasets: [{
          label: 'Sold Amount',
          data: data,
          backgroundColor: backgroundColors,
        }],
      };
    },

    updateWarehouseChartData() {
      const warehousesToDisplay = this.showAllWarehouses ? this.warehouses : this.warehouses.slice(0, 4); // Show top 4 warehouses or all warehouses
      const labels = warehousesToDisplay.map(warehouse => warehouse.product.product_name);
      const data = warehousesToDisplay.map(warehouse => warehouse.available_quantity);
      const backgroundColors = this.generateRandomColors(warehousesToDisplay.length);

      this.warehouseChartData = {
        labels: labels,
        datasets: [{
          label: 'Available Quantity',
          data: data,
          backgroundColor: backgroundColors,
        }],
      };
    },
    toggleShowAll(type) {
      if (type === 'stores') {
        this.showAllStores = !this.showAllStores;
        this.updateStoreChartData();
      } else if (type === 'warehouses') {
        this.showAllWarehouses = !this.showAllWarehouses;
        this.updateWarehouseChartData();
      }
    }
  },
};
</script>
<style scoped>
.card {
  background-color: var(--menu-background-color);
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  margin-bottom: 20px;
  width: 45%;
  height: 100%;
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
