<template>
  <section class="contact">
    <div class="container">
      <h1>Contact Us</h1>
      <p>Get in touch and we'll be happy to answer your questions.</p>
      <form @submit.prevent="handleSubmit">
        <div class="field">
          <label for="name">Name</label>
          <input type="text" id="name" v-model="name" required>
        </div>
        <div class="field">
          <label for="email">Email</label>
          <input type="email" id="email" v-model="email" required>
        </div>
        <div class="field">
          <label for="message">Message</label>
          <textarea id="message" v-model="message" required></textarea>
        </div>
        <button type="submit" class="button is-primary">Send Message</button>
      </form>
      <p>You can also reach us at:</p>
      <ul>
        <li>Email: support@krypton.com</li>
        <li>Phone: +92 (300) - 0000000</li>
      </ul>
    </div>
  </section>
</template>

<script>
export default {
  name: 'ContactView',
  data() {
    return {
      name: '',
      email: '',
      message: '',
    };
  },
  methods: {
    handleSubmit() {
      // Handle form submission logic here
      // (e.g., send email, display success message)
      console.log('Form submitted:', this.name, this.email, this.message);
      this.name = '';
      this.email = '';
      this.message = '';
    },
  },
};
</script>

<style scoped>
.contact {
  padding: 5rem 0;
  text-align: center;
}

.contact form {
  display: flex;
  flex-direction: column;
  width: 50%;
  margin: 0 auto;
}

.contact .field {
  margin-bottom: 1rem;
}

.contact .field label {
  display: block;
  margin-bottom: 0.5rem;
}

.contact button {
  margin-top: 1rem;
}

@media (max-width: 768px) {
  .contact form {
    width: 100%;
  }
}
</style>
