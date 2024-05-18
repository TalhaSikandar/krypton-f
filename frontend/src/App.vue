<template>
  <div class="site-container" style="max-width: 80%; margin: 0 auto">
    <div class="navbar-containter">
      <nav class="navbar is-dark">
        <div class="navbar-brand">
          <router-link :to="{name: 'home'}" class="navbar-item"><strong>Krypton</strong></router-link>
          <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="nav-bar-menu" @click="showMobileMenu = !showMobileMenu">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>

        <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
          <div class="navbar-end">
            <router-link to="/dashboard" class="navbar-item">Dashboard</router-link>

            <div class="navbar-item">
              <div class="buttons">
                <router-link to="/login" class="button is-light">Login</router-link>
              </div>
            </div>
          </div>
        </div>
      </nav>
    </div>

  <div class="section">
    <router-view/>
  </div>
    <div class="footer-container">
      <footer class="footer">
        <p class="has-text-centered">Krypton Securities since 2024</p>
      </footer>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      showMobileMenu: false,
    }
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';
</style>


