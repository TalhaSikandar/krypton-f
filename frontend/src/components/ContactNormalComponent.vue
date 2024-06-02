<template>
  <div>
    <label class="label" for="contact_no">Contact Number</label>
    <input class="input" type="text" id="contact_no" v-model="contact.contact_no" placeholder="Enter contact number" />

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
        console.log(newVal)
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
