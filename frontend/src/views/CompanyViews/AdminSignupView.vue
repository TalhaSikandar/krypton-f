
<template>
  <div class="main_container">
  <div class="container">
    <h1 class="heading">Admin Signup</h1>
    <div class="signup_form">
    <form @submit.prevent="submitAdminForm">
      <div class="field">
        <label class="label">Email</label>
        <div class="control">
          <input class="input" v-model="admin.email" type="email" required>
        </div>
      </div>
      <div class="field">
        <label class="label">Username</label>
        <div class="control">
          <input class="input" v-model="admin.username" type="text" required>
        </div>
      </div>
      <div class="field">
        <label class="label">Password</label>
        <div class="control">
          <input class="input" v-model="admin.password1" type="password" required>
        </div>
      </div>
      <div class="field">
        <label class="label">Confirm Password</label>
        <div class="control">
          <input class="input" v-model="admin.password2" type="password" required>
        </div>
      </div>
      <button class="button is-primary" type="submit">Sign Up</button>
    </form></div>
  </div></div>
</template>

<script>
import axios from 'axios';
import { toast } from 'bulma-toast';

export default {
  name: 'AdminSignup',
  data() {
    return {
      admin: {
        email: '',
        username: '',
        password1: '',
        password2: '',
        company_id: this.$route.params.company_id,
        role: 'ADMIN'
      }
    };
  },
  
  mounted() {
    document.title = 'Admin Signup | Krypton'
  },
  methods: {
    getCsrfToken() {
      axios.get('/companies/csrf/')
        .then(response => {
          axios.defaults.headers.common['X-CSRFToken'] = response.data.csrfToken;
        });
    },
    submitAdminForm() {
      if (!localStorage.getItem("company_id"))
        localStorage.setItem("company_id", 29)
      if (this.admin.password1 !== this.admin.password2) {
            toast({
              message: 'Passwords do not match!',
              type: 'is-danger',
              duration: 5000,
              dismissible: true
            });
            return;
          }
      this.admin.company_id = localStorage.getItem("company_id")
      localStorage.removeItem("company_id")
      axios.post('/accounts/admin_signup/', this.admin)
        .then(response => {
          if (response.status === 201) { // Check for successful response
            console.log("Admin Added:", response.data); // Log actual data
            localStorage.setItem("username", response.data.username); // Assuming username exists
          this.$router.push({ name: 'signin' });
          } else {
            toast({
              message: 'Error signing up admin: Unexpected response', // Generic error message
              type: 'is-danger',
              duration: 5000,
              pauseOnHover: true,
              dismissible: true
            });
          }
        })
        .catch(error => {
          toast({
            message: 'Error signing up admin: ' + JSON.stringify(error.response),
            type: 'is-danger',
            duration: 5000,
            pauseOnHover: true,
            dismissible: true
          });
        });
    }
  },
  created() {
    this.getCsrfToken();
  }
};
</script>

<style scoped>
<style scoped>
.main_container{
  display:flex;
}
.container {
  margin-top: 10rem;
  max-width: 25%;
  max-height: 100%;
  border-radius: 2rem;
}

.signup_form {
  display: flex;
  margin: auto 0;
  justify-content: center;
  align-items: center;
}
</style>
