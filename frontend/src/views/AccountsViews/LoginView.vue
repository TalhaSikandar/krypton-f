<template>
  <div class="login-container" style="min-height: 750px; display: flex; justify-content: center; align-items: center;">
    <div class="card login-card">
      <header class="card-header">
        <p class="card-header-title">
          Login Form
        </p>
      </header>
      <div class="card-content">
        <div v-if="successMessage">
          <p class="has-text-success">{{ successMessage }}</p>
        </div>
        <div v-if="errorMessage">
          <p class="has-text-danger">{{ errorMessage }}</p>
        </div>
        <form @submit.prevent="submitLoginForm">
          <div class="field">
            <label class="label" for="loginEmail">Email</label>
            <div class="control">
              <input class="input is-medium is-rounded" v-model="login.email" type="email" id="loginEmail" required>
            </div>
          </div>
          <div class="field">
            <label class="label" for="loginPassword">Password</label>
            <div class="control">
              <input class="input is-medium is-rounded" v-model="login.password" type="password" id="loginPassword" required>
            </div>
          </div>
          <div class="field">
            <p>
              Don't have a company account?
              <router-link :to="{ name: 'companySignup' }" class="has-text-link">Register your company</router-link>
            </p>
          </div>
          <div class="myButton is-centered">
            <button class="button is-primary is-rounded" type="submit">Login</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { toast } from 'bulma-toast';
import { mapActions, mapGetters } from 'vuex'; // Import for Vuex integration

export default {
  name: 'LoginView',
  data() {
    return {
      login: { // Object to hold login credentials
        email: '',
        password: '',
      },
      successMessage: null,
      errorMessage: null,
    };
  },
  mounted() {
    document.title = 'Login | Krypton';
  },
  methods: {

    ...mapActions(['login']), // Use mapActions to access login action

    async submitLoginForm() {
      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("access_token")
      console.log(this.login.email)
      console.log(this.login.password)
      try {

        const response = await axios.post('/accounts/api/token/', {
          username: this.login.email,
          password: this.login.password,
        });
        

        const token = response.data.access_token;
        this.$store.commit('setToken', token)

        const username = response.data.username; // Adjust based on your API response
        localStorage.setItem("username", username)

        const company_name = response.data.company_name
        localStorage.setItem("company_name", company_name)
        // this.$store.status.username = username;

        localStorage.setItem("access_token", token)
        axios.defaults.headers.common["Authorization"] = "access_token" + token;
        console.log(token)

        this.successMessage = 'Logged In';
        toast({
          message: this.successMessage,
          type: 'is-success',
          duration: 2000,
          dismissible: true,
          position: 'top-center',
        });
        this.$router.push('/dashboard'); // Replace with your dashboard route

      } catch (error) {

        this.errorMessage = 'Invalid email or password';
        toast({
          message: this.errorMessage,
          type: 'is-danger',
          duration: 5001,
          dismissible: true,
          position: 'bottom-right',

        });
      }
    }
  },
  computed: {
    ...mapGetters(['isAuthenticated']), // Use mapGetters to access authenticated getter from store
  },
};
</script>

<style scoped>
.login-card {
  min-height: 400px;
  min-width: 400px;
  margin: 0 auto;
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.field {
  margin-bottom: 1rem;
}

.myButton {
  margin: 0 auto !important;
  width: 100%;

}

.button {
  width: 50%;
}
</style>
