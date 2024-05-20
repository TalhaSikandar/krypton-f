
<template>
  <div class="container">
    <h1>Admin Signup</h1>
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
    </form>
  </div>
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
  methods: {
    getCsrfToken() {
      axios.get('/companies/csrf/')
        .then(response => {
          axios.defaults.headers.common['X-CSRFToken'] = response.data.csrfToken;
        });
    },
    submitAdminForm() {
      if (this.admin.password1 !== this.admin.password2) {
            toast({
              message: 'Passwords do not match!',
              type: 'is-danger',
              duration: 5000,
              dismissible: true
            });
            return;
          }
      axios.post('/accounts/admin_signup/', this.admin)
        .then(response => {
          this.$router.push({ name: 'login' });
        })
        .catch(error => {
          toast({
            message: 'Error signing up admin: ' + JSON.stringify(error.response.data),
            type: 'is-danger',
            duration: 5000,
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
