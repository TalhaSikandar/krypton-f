// store/index.js
import { createStore } from 'vuex';

const store = createStore({
  state: {
    authenticated: !!localStorage.getItem('access_token'),
    isLoading: false,
    username: localStorage.getItem('username') || '',
    token: localStorage.getItem('access_token') || '',
    company_name: localStorage.getItem('company_name') || '',
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
    setUsername(state, username) {
      state.username = username;
    },
    setToken(state, token) {
        state.token = token;
        state.authenticated = true;
    },
    removeToken(state, token) {
        state.token = '';
        state.authenticated = false;
        state.username = '';
    },
  },
  actions: {
    login({ commit }, { token, username }) {
      commit('setToken', token);
      commit('setUsername', username);
      localStorage.setItem('access_token', token);
      localStorage.setItem('username', username);
      axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
    },
    logout({ commit }) {
      commit('removeToken');
      localStorage.removeItem('access_token');
      localStorage.removeItem('username');
      delete axios.defaults.headers.common['Authorization'];
    },
  },
});

export default store;
