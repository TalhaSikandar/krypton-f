
<template>
  <div class="container">
    <h1>Company Signup</h1>
    <form @submit.prevent="submitCompanyForm">
      <div class="field">
        <label class="label">Company Name</label>
        <div class="control">
          <input class="input" v-model="company.company_name" type="text" required>
        </div>
      </div>
      <div class="field">
        <ContactComponent :contact="company.contact" />
        <AddressComponent :address="company.address" />
      </div>
      <div class="field">
        <label class="label">Industry</label>
        <div class="control">
          <input class="input" v-model="company.industry" type="text">
        </div>
      </div>
      <div class="field">
        <label class="label">Description</label>
        <div class="control">
          <textarea class="textarea" v-model="company.description"></textarea>
        </div>
      </div>
      <button class="button is-primary" type="submit" @click="submitCompanyForm">Sign Up</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import { toast } from 'bulma-toast';
import ContactComponent from '../../components/ContactComponent.vue';
import AddressComponent from '../../components/AddressComponent.vue';

export default {
  components: {
    ContactComponent,
    AddressComponent,
  },
  name: 'CompanySignup',
  data() {
    return {
      company: {
        company_name: '',
        contact: {
          contact_no: '',
          email: '',
          website: '',
        },
        address: {
          city: '',
          country: '',
        },
        industry: '',
        description: '',
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
    submitCompanyForm() {
      axios.post('/companies/signup/', this.company)
        .then(response => {
      console.log(this.company)
          this.$router.push({ name: 'adminSignup', params: { company_id: response.data.company_id } });
        })
        .catch(error => {
          console.log(this.company)
          toast({
            message: 'Error signing up company: ' + JSON.stringify(error.response.data),
            type: 'is-danger',
            duration: 5000,
            dismissible: true,
            animate: { in: 'fadeIn', out: 'fadeOut' },
          });
        });
    },
    updateContact(contactData) {
      this.company.contact = contactData;
    },
    updateAddress(addressData) {
      this.company.address = addressData;
    }
  },
  created() {
    this.getCsrfToken();
  }
};
</script>
