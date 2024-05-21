<template>
  <div v-if="showLogoutCard" class="modal is-active">
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Confirm Logout</p>
        <button class="delete" aria-label="close" @click="$emit('closeLogoutCard')"></button>
      </header>
      <section class="modal-card-body">
        <p>Are you sure you want to logout?</p>
      </section>
      <footer class="modal-card-foot">
        <button class="button is-danger" @click="$emit('logoutConfirmed')">Logout</button>
        <button class="button" @click="$emit('closeLogoutCard')">Cancel</button>
      </footer>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    showLogoutCard: Boolean, // Receive the showLogoutCard prop from the parent component
  },
  methods: {
    // No methods required in this component
  },
};
</script>

<style scoped>
.modal-card {
  max-width: 500px;
}
</style>
