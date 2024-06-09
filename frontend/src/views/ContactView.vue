<template>
  <div class="contact-form">
    <div class="container">
      <div class="form-wrapper">
        <h1 class="title">Write us</h1>
        <p class="description">We're open for any suggestion or just to have a chat</p>
        <form @submit.prevent="handleSubmit">
          <div class="field">
            <label for="name" class="label">Name</label>
            <input type="text" id="name" v-model="name" class="input" required>
          </div>
          <div class="field">
            <label for="email" class="label">Email</label>
            <input type="email" id="email" v-model="email" class="input" required>
          </div>
          <div class="field">
            <label for="subject" class="label">Subject</label>
            <input type="text" id="subject" v-model="subject" class="input">
          </div>
          <div class="field">
            <label for="message" class="label">Message</label>
            <textarea id="message" v-model="message" class="input" required></textarea>
          </div>
          <div class="field">
            <button type="submit" class="button is-primary">Send Message</button>
          </div>
        </form>
      </div>
        <div class="contact-info">
          <p class="info-label">Contact Information</p>
          <ul>
            <li><span class="info-label">Address:</span> Arfa Technology Park, Lahore</li>
            <li><span class="info-label">Phone:</span> +1235 2355 98</li>
            <li><span class="info-label">Email:</span> support@krypton.com</li>
            <li><span class="info-label">Website:</span> krypton.com</li>
          </ul>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ContactForm',
  data() {
    return {
      name: '',
      email: '',
      subject: '',
      message: '',
    };
  },
  methods: {
    handleSubmit() {
      // Implement your form submission logic here
      console.log('Form submitted:', this.name, this.email, this.subject, this.message);

      // Clear the form fields after submission
      this.name = '';
      this.email = '';
      this.subject = '';
      this.message = '';
    },
  },
};
</script>

<style scoped>
.contact-form {
  background-color: #f0f2f5; /* Light gray background */
  padding: 8rem 0; /* Increased padding for better spacing */
  text-align: center;
}

.contact-form .container {
  max-width: 700px; /* Maintains maximum width */
  margin: 0 auto; /* Centers the form horizontally */
  border-radius: 10px; /* Rounded corners for a softer look */
  background-color: #fff; /* White background for the form section */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2); /* Subtle shadow for depth */
}

.contact-form .form-wrapper {
  margin-top: 4rem auto; /* Centers the form horizontally */
  padding: 3rem; /* Padding within the form section */
  color: var(--menu-background-color);
}

.contact-form .title {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #333; /* Darker text color for better contrast */
}

.contact-form .description {
  font-size: 1.2rem;
  color: #666; /* Lighter text color for description */
  margin-bottom: 2rem;
  line-height: 1.5; /* Increased line height for better readability */
}

.contact-form .field {
  margin-bottom: 1.5rem; /* Adjusted spacing between fields */
}

.contact-form .field .label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
  color: #333; /* Darker text color for labels */
}

.contact-form .field .input,
.contact-form .field .textarea {
  padding: 0.8rem;
  border: 1px solid #ccc; /* Lighter border color */
  border-radius: 4px;
  width: 200px;
  box-sizing: border-box;
  font-size: 1rem;
}

.contact-form .contact-info {
  margin-top: 2rem;
  padding: 2rem; /* Padding for the contact information section */
  border-top: 1px solid #ddd; /* Divider line between form and info */
  background-color: var(--menu-background-color);
}

.info-label {
  color: white; /* Darker text color for contact information labels */
  font-weight: bold;
  margin-bottom: 0.5rem;
}
.contact-info{
  margin: 0 auto;

}
</style>
