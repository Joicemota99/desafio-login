import { createRouter, createWebHistory } from "vue-router";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import Sucess from "../views/Sucess.vue"

const routes = [
  { path: "/", redirect: "/login" }, // Redireciona a rota raiz para login
  { path: "/login", component: Login },
  { path: "/register", component: Register },
  { path: "/sucess", component: Sucess}
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
