<template>
  <section class="about">
    <div class="container">
      <div class="about-hero">
        <img src="../assets/about-hero-img.jpg" alt="About Us Hero Image">
        <div class="about-hero-content">
          <h1>Empowering Businesses, One Dashboard at a Time</h1>
          <p>Simplify your operations and streamline your workflow with our all-in-one dashboard solution.</p>
        </div>
      </div>
      <div class="about-content">
        <h2>Our Story</h2>
        <p>
          [Insert a brief description of your company's origin story, its founding principles, or the inspiration behind your dashboard solution.]
        </p>
        <h2>What We Do</h2>
        <p>
          We provide an intuitive and powerful dashboard that helps businesses like yours manage their [list key areas your dashboard helps with, e.g., products, raw materials, inventory, orders]. Our platform simplifies complex processes, giving you a central hub to:
        </p>
        <ul class="features">
          <li>[Feature 1 benefit]</li>
          <li>[Feature 2 benefit]</li>
          <li>[Feature 3 benefit]</li>
        </ul>
        <h2>Why Choose Us?</h2>
        <p>
          We differentiate ourselves by offering [list unique selling points, e.g., user-friendliness, scalability, robust features, integrations]. Our commitment to [mention your core values, e.g., innovation, customer satisfaction] ensures you receive a product that not only meets but exceeds your expectations.
        </p>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'AboutView',
};
</script>

<style scoped>
.about {
  padding: 5rem 0;
}

.about-hero {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: #f5f5f5;
  padding: 5rem;
  position: relative;
}

.about-hero img {
  width: 50%;
  height: auto;
  object-fit: cover;
  border-radius: 5px;
}

.about-hero-content {
  text-align: center;
  color: #333;
  z-index: 2;
}

.about-hero-content h1 {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.about-content {
  padding-top: 5rem;
}

.about-content p {
  line-height: 1.5;
  margin-bottom: 2rem;
}

.features li {
  margin-bottom: 1rem;
}

@media (max-width: 768px) {
  .about-hero {
    flex-direction: column;
    text-align: center;
  }

  .about-hero img {
    width: 100%;
    margin-bottom: 2rem;
  }
}
</style>
