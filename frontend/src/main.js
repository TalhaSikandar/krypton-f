import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

import './global.css'

axios.defaults.baseURL = 'http://127.0.0.1:8000/'

createApp(App).use(store).use(router, axios).mount('#app')


// Improved Token-Based Authentication with Axios Interceptors

// Configure Axios defaults (optional, can be outside interceptor creation)
axios.defaults.headers.common['Content-Type'] = 'application/json'; // Set default content type

const instance = axios.create({
  baseURL: 'http://127.0.0.1:8000/',
});

instance.interceptors.request.use(config => {
  const accessToken = localStorage.getItem('access_token');
  if (accessToken) {
    config.headers.Authorization = `Bearer ${accessToken}`;
  }
  return config;
}, error => {
  return Promise.reject(error);
});

instance.interceptors.response.use(response => {
  return response;
}, async error => {
  const originalRequest = error.config;
  if (error.response.status === 401 && !originalRequest._retry) {
    originalRequest._retry = true;
    const refreshToken = localStorage.getItem('refresh_token');
    if (refreshToken) {
      try {
        const response = await axios.post('/accounts/api/token/refresh/', { refresh: refreshToken });
        if (response.status === 200) {
          localStorage.setItem('access_token', response.data.access);
          instance.defaults.headers.common['Authorization'] = `Bearer ${response.data.access}`;
          return instance(originalRequest); // Retry the original request with new access token
        }
      } catch (e) {
        console.error('Refresh token failed:', e);
        // Handle failed refresh (e.g., logout user)
      }
    }
  }
  return Promise.reject(error);
});

export default instance; // Export the modified instance for potential global usage
