import { createApp } from 'vue';
import App from './App.vue';
import './registerServiceWorker';
import router from './router';
import './supabase';
import '@/db'

export const AXIOS_BASE_URL = process.env.VUE_APP_AXIOS_BASE_URL

createApp(App).use(router).mount('#app');
