// store/index.js
import { createStore } from 'vuex';

const store = createStore({
  state: {
    authenticated: false,
    isLoading: false,
    token: '',
  },
  mutations: {
    initializeAccount(state) {
      if(localStorage.getItem('access_token')) {
        state.token = localStorage.getItem('access_token');
        state.authenticated = true;
      }
      else {
        state.token = '';
        state.authenticated = false;
      }
    },
    authenticateUser(state, status) {
      state.authenticated = status;
    },
    setToken(state, token) {
        state.token = token;
        state.authenticated = true;
    },
    removeToken(state, token) {
        state.token = '';
        state.authenticated = false;
    },
  },
  actions: {
  },
});

export default store;
