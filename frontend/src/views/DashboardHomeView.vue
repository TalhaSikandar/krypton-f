<template>
  <div class="dashboard-area">
    <aside class="menu">
      <ul class="side-menu">
        <div class="dashboard_start" style="display: flex; flex-direction: column; align-items:center; gap: 0rem;">
        <h1 class="dashboard-heading">Dashboard</h1>
        <span>-</span>
        <h1> <span class="comany_name" style="color: var(--primary-color); margin-bottom: 4rem; font-size: 1.2rem; font-weight:bold;">{{ company_name }}</span></h1>
        </div>
        <div class="main-routes">
          <li>
            <router-link :to="{ name: 'dashboardhome' }" exact :class="{ 'is-active': $route.name === 'dashboardhome' }">
              <div class="icon-container">
                <i class="fas fa-home"></i>
                <span class="menu-text">Home</span>
              </div>
            </router-link>
          </li>
          <li>
            <router-link :to="{ name: 'stores' }" exact :class="{ 'is-active': $route.name === 'stores' }">
              <div class="icon-container">
                <i class="fas fa-store"></i>
                <span class="menu-text">Stores</span>
              </div>
            </router-link>
          </li>
          <li>
            <router-link :to="{ name: 'warehouses' }" exact :class="{ 'is-active': $route.name === 'warehouses' }">
              <div class="icon-container">
                <i class="fas fa-warehouse"></i>
                <span class="menu-text">Warehouses</span>
              </div>
            </router-link>
          </li>
          <li>
            <router-link :to="{ name: 'suppliers' }" exact :class="{ 'is-active': $route.name === 'suppliers' }">
              <div class="icon-container">
                <i class="fas fa-truck"></i>
                <span class="menu-text">Suppliers</span>
              </div>
            </router-link>
          </li>
          <li>
            <router-link :to="{ name: 'employees' }" exact :class="{ 'is-active': $route.name === 'employees' }">
              <div class="icon-container">
                <i class="fas fa-users"></i>
                <span class="menu-text">Employees</span>
              </div>
            </router-link>
          </li>
        </div>
      </ul>
      <ul class="side-menu">
        <div class="settings-routes">
          <li>
            <hr class="separator"> </li>
          <li>
            <router-link :to="{ name: 'settings' }" exact :class="{ 'is-active': $route.name === 'settings' }">
              <div class="icon-container">
                <i class="fas fa-cogs"></i>
                <span class="menu-text">Settings</span>
              </div>
            </router-link>
          </li>
          <li>
            <button>
              <div class="icon-container" @click="handleLogout()">
                <i class="fas fa-sign-out"></i>
                <span class="menu-text">Logout</span>
              </div>
            </button>
          </li>
        </div>
      </ul>
    </aside>
    <main class="content" style="margin: 24px 0px" >
      <router-view />
    </main>
  </div>
</template>
<script>
import { mapState } from 'vuex';

export default {
  computed: {
    ...mapState(['company_name']),
  },
  methods: {
    handleLogout() {
      // Handle logout logic (e.g., clear local storage, dispatch logout action)
      this.$store.commit('removeToken')
      // Clear local storage (optional)
      localStorage.removeItem('access_token');
      localStorage.removeItem('username');
      localStorage.removeItem('company_name'); // Avoid storing password in local storage
      // Redirect to login page after logout
      this.$router.push({ name: 'home' });
    },
  },
  mounted() {
    document.title = 'Dashboard | Krypton';
    this.$router.push({ name: 'dashboardhome' }); // Replace with your dashboard route
  },
};
</script>

<style scoped>


/* Light theme styles */
.light {
  --background-color: #f5f5f5; /* Light background color */
  --menu-background-color: #f0f0f0; /* Light menu background color */
  --text-color: #333; /* Light text color */
}

/* Dark theme styles (already defined in base styles) */
.dashboard-area {
  height: 100vh;
  width: 100%;
  display: flex;
  background-color: var(--background-color);
  font-family: var(--font-family);
}

.menu {
  width: 240px;
  background-color: var(--menu-background-color);
  padding: 0rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  border: 1px solid var(--border-color);
  margin: 24px 0px;
  border-top-right-radius: 2rem;
  border-bottom-right-radius: 2rem;
}

.menu .title {
  color: var(--text-color-titles);
  margin-bottom: 1rem;
}

.menu-list {
  list-style: none;
  padding: 0;
  width: 160px;
}

.menu-list li {
  width: 100%;
  margin: 0.5rem 0;
  display: flex;
  justify-content: center;
}

.menu-list li a:hover .icon-container,
.menu-list li a.is-active .icon-container {
  background-color: var(--primary-color);
}

.icon-container {
  display: flex;
align-items: center; /* Center icons vertically (already defined) */
  justify-content: left; /* Center icons horizontally (added) */
  padding: 0.1rem 1rem; /* Add some padding for spacing */
  height: 48px;
  min-width: 172px; /* Remove fixed width, let content determine width */
  background-color: var(--menu-background-color); /* Or use var(--menu-background-color) for theme inheritance */
  border-radius: 2px;
  transition: background-color 0.3s;
  gap: 1rem;
}
.icon-container i {
  font-size: 1.2rem; /* Adjust font size for smaller icons */
  color: var(--text-color);
}

.content {
  flex: 1;
  padding: 1rem;
  background-color: var(--background-color);
  border-radius: 5px;
}

.separator {
  border: none;
  height: 1px;
  background-color: var(--border-color);
  margin: 1rem 0;
}

.side-menu {
  list-style: none; /* Remove default bullet points */
  padding: 0; /* Remove default padding */
  margin: 0; /* Remove default margin */
  width: 200px; /* Adjust width as needed */
  display: flex;
  flex-direction: column;
  background-color: var(--menu-background-color); /* Adjust background color */
  color: var(--white-background-color); /* Adjust text color */
  /* gap: 2rem; */
  /* flex-wrap: nowrap; */
  justify-content: space-between !important;
  /* align-items: normal; */
  /* align-content: normal; */
}
.side-menu li {
  margin: 0rem 0; /* Adjust spacing between items */
}

.side-menu a {
  text-decoration: none; /* Remove underline */
  color: inherit; /* Inherit text color from parent */
  display: flex;
  align-items: center;
  padding: 0rem; /* Adjust padding */
  transition: background-color 0.3s ease; /* Smooth background color transition */
}

.side-menu a:hover {
  background-color: #333333; /* Adjust hover background color */
}

.side-menu a.is-active {
  background-color: var(--accent-color, #9d4edd); /* Use primary color if defined, otherwise fallback */
  font-weight: bold; /* Optional: Make active link bolder */
}

.dashboard-heading {
  font-size: 1.2rem; /* Adjust font size */
  text-align: center; /* Center the text */
  font-weight: thin; /* Make it bold */
  margin-bottom: 1rem; /* Add some margin */
  margin-top: 2rem; /* Add some margin */
  /* Separate styles for company name and dashboard text */
  display: flex; /* Make it a flex container */
  gap: 0.5rem; /* Add some space between elements */
}
.company_name {
  font-weight: heavy;
}
.settings-routes {
  margin-bottom:2rem;
}


</style>
