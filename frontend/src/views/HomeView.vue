<template>
  <section class="hero">
    <div class="hero-container">
      <div class="hero-content">
        <h1>Empower Your Business</h1>
        <p>
          Simplify your operations and streamline your workflow with our all-in-one dashboard. Manage products, raw materials, and more, all in one central location.
        </p>
        <router-link :to="{name: 'companySignup'}" class="button is-primary">Get Started</router-link>
      </div>
      <div class="hero-image">
        <img src="../assets/hero-img.jpg" alt="Hero Image">
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'HomeView',
};
</script>

<style scoped>
.hero {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 70vh;
  background-color: #f5f5f5;
}

.hero-container {
  display: flex;
  max-width: 1024px;
  width: 80%;
  margin: 0 auto;
  align-items: center;
  justify-content: space-between;
  gap: 4rem;
}

.hero-content {
  text-align: center;
  color: #333;
}

.hero-content h1 {
  font-size: 2rem;
  margin-bottom: 2rem;
}
.hero-content p {
  margin-bottom: 2rem;
}

.hero-image img {
  width: 100%;
  height: auto;
  object-fit: cover;
}

@media (max-width: 768px) {
  .hero-content {
    text-align: left;
  }

  .hero-image {
    display: none;
  }
}
</style>
