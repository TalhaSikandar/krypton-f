import { createRouter, createWebHistory } from 'vue-router'
import DashboardHomeView from '../views/DashboardHomeView.vue'
import DashboardSectionView from '../views/DashboardSectionView.vue'
import StoreView from '../views/StoreView.vue'
import WarehouseView from '../views/WarehouseView.vue'
import EmployeeView from '../views/EmployeeView.vue'
import SupplierView from '../views/SupplierView.vue'
import SettingsView from '../views/SettingsView.vue'
import LoginView from '../views/LoginView.vue'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/dashboard',
    name: 'dashboardhome',
    component: DashboardHomeView,
    children: [
        {
          path: '/',
          name: 'dashboadsection',
          component: DashboardSectionView
        },
        {
          path: '/stores',
          name: 'stores',
          component: StoreView
        },
        {
          path: '/warehouses',
          name: 'warehouses',
          component: WarehouseView
        },
        {
          path: '/suppliers',
          name: 'suppliers',
          component: SupplierView
        },
        {
          path: '/employees',
          name: 'employees',
          component: EmployeeView
        },
        {
          path: '/settings',
          name: 'settings',
          component: SettingsView
        },
    ]
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue') // also syntax
  },
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  // {
  //   path: '/stores',
  //   name: 'stores',
  //   component: StoreView
  // },
  // {
  //   path: '/warehouses',
  //   name: 'warehouses',
  //   component: WarehouseView
  // },
  // {
  //   path: '/suppliers',
  //   name: 'suppliers',
  //   component: SupplierView
  // },
  // {
  //   path: '/employees',
  //   name: 'employees',
  //   component: EmployeeView
  // },
  // {
  //   path: '/settings',
  //   name: 'settings',
  //   component: SettingsView
  // },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
