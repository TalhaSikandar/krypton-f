import axios from 'axios';
export function initializeAccount({ commit, state }) {
  commit('initializeAccount');
  const token = state.token;

  if (token) {
    axios.defaults.headers.common['Authorization'] = "access_token " + token;
  } else {
    axios.defaults.headers.common['Authorization'] = "";
  }
}
