<template>
  <div class="login-form">
    <h1 class="title">Login Form</h1>
    <form @submit.prevent="submitLoginForm">
      <div class="field">
        <label class="label">Email</label>
        <div class="control">
          <input class="input" v-model="login.email" type="email" required>
        </div>
      </div>
      <div class="field">
        <label class="label">Password</label>
        <div class="control">
          <input class="input" v-model="login.password" type="password" required>
        </div>
      </div>
      <button class="button is-primary" type="submit">Login</button>
    </form>
  </div>
</template>


<script>
import axios from 'axios';
import { toast } from 'bulma-toast';

export default {
  name: 'LoginView',
  data() {
    return {
      login: {
        email: '',
        password: ''
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
    submitLoginForm() {
      axios.post('/accounts/login/', this.login)
        .then(response => {
          if (response.data.redirect_url) {
            this.$router.push(response.data.redirect_url);
          } else {
            toast({
              message: 'Logged in successfully',
              type: 'is-success',
              duration: 5000,
              dismissible: true
            });
          }
        })
        .catch(error => {
          toast({
            message: 'Invalid email or password',
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

<style scoped>
.login-form {
  max-width: 400px;
  margin: 0 auto;
  padding: 1rem;
}

.title {
  text-align: center;
}

.field {
  margin-bottom: 1rem;
}

.button {
  width: 100%;
}
</style>
