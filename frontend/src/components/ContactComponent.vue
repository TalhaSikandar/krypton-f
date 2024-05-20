<template>
  <div>
    <label class="label" for="contact_no">Contact Number</label>
    <input class="input" type="text" id="contact_no" v-model="contact.contact_no" placeholder="Enter contact number" />

    <label class="label" for="email">Email</label>
    <input class="input" type="email" id="email" v-model="contact.email" placeholder="Enter email" />

    <label class="label" for="website">Website</label>
    <input class="input" type="url" id="website" v-model="contact.website" placeholder="Enter website URL" />
  </div>
</template>

<script>
export default {
  props: {
    contact: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      contactData: this.contact,
    };
  },
  watch: {
    contactData: {
      handler(newVal) {
        this.$emit('update-contact', newVal);
      },
      deep: true,
    },
  },
};
</script>

<style scoped>
/* Add your styles here */
</style>
