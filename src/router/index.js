import { createRouter, createWebHistory } from 'vue-router';
import MainView from '../views/MainView.vue';
import ClipsView from '../views/ClipsView.vue';

const routes = [
  {
    path: '/',
    name: 'main',
    component: MainView,
  },
  {
    path: '/clips',
    name: 'clips',
    component: ClipsView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
