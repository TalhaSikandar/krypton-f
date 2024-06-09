<template>
  <div>
    <label class="label" for="country">Country</label>
    <input class="input" type="text" id="country" v-model="selectedCountry" placeholder="Select country" @focus="getCountries" />
    <ul v-if="showCountryDropdown" class="dropdown">
      <li class="dropdown-item" v-for="country in countries" :key="country.name" @click="selectCountry(country.name)">{{ country.flag }} {{ country.name }}</li>
    </ul>

    <label class="label" for="city">City</label>
    <input class="input" type="text" id="city" v-model="address.city" placeholder="Enter city" />
    <ul v-if="showCityDropdown" class="dropdown">
      <li v-for="city in filteredCities" :key="city" @click="selectCity(city)">{{ city }}</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    address: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      selectedCountry: '',
      showCountryDropdown: false,
      showCityDropdown: false,
      addressData: this.address,
      countries: [],
      citiesByCountry: {},
    };
  },
  computed: {
    filteredCities() {
      return this.citiesByCountry[this.selectedCountry] || [];
    },
  },
  methods: {
    async getCountries() {
      try {
        const response = await axios.get('https://restcountries.com/v3.1/all');
        const countries = response.data.map(country => ({
          name: country.name.common || '', // Official name of the country
          flag: country.flag,
        }));
        countries.sort((a, b) => a.name.localeCompare(b.name));
        this.countries = countries;
        this.showCountryDropdown = true;
      } catch (error) {
        console.error('Error fetching countries:', error);
      }
    },
    async getCitiesByCountry(country) {
      try {
        const response = await axios.post('https://countriesnow.space/api/v0.1/countries/cities', {
          country: country
        });
        const cities = response.data.data || [];
        this.citiesByCountry = cities;
        this.selectedCountry = country;
        this.showCountryDropdown = false;
        this.showCityDropdown = true;
      } catch (error) {
        console.error('Error fetching cities:', error);
      }
    },
    selectCountry(country) {
      this.selectedCountry = country;
      if (!this.citiesByCountry[country]) {
        this.getCitiesByCountry(country);
      } else {
        this.showCityDropdown = true;
        this.showCountryDropdown = false;
      }
    },
    selectCity(city) {
      this.address.city = city;
      this.showCityDropdown = false;
    },
  },
  watch: {
    addressData: {
      handler(newVal) {
        this.$emit('update-address', newVal);
      },
      deep: true,
    },
  },
};
</script>

<style scoped>
.dropdown {
  display: flex;
  flex-direction: column;
  list-style-type: none;
  padding-left: 0;
  border: 1px solid #ccc;
  border-radius: 4px;
  max-height: 150px;
  overflow-y: auto;
}

.dropdown-item {
  color: black;
  cursor: pointer;
}

.dropdown li {
  padding: 5px 10px;
  cursor: pointer;
}

.dropdown li:hover {
  background-color: #f0f0f0;
}
</style>
