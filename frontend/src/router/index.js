import { createRouter, createWebHistory } from 'vue-router'
import DashboardHomeView from '../views/DashboardHomeView.vue'
import DashboardSectionView from '../views/DashboardSectionView.vue'
import StoreView from '../views/StoreViews/StoreView.vue'
import WarehouseView from '../views/WarehouseViews/WarehouseView.vue'
import EmployeeView from '../views/EmployeeView.vue'
import SupplierView from '../views/SupplierView.vue'
import SettingsView from '../views/SettingsView.vue'
import HomeView from '../views/HomeView.vue'

import CompanySignupView from '../views/CompanyViews/CompanySignupView.vue'
import AdminSignupView from '../views/CompanyViews/AdminSignupView.vue'

import LoginView from '../views/AccountsViews/LoginView.vue'

import store from '../store'
import { initializeAccount } from '../store/action'; // Adjust the path as necessary
import Router from 'vue-router';

const routes = [
  {
    path: '/dashboard',
    name: 'dashboard',
    component: DashboardHomeView,
    meta: {
      requiredLogin: true,
    },
    children: [
        {
          path: '/dashboard/home/',
          name: 'dashboardhome',
          component: DashboardSectionView
        },
        {
          path: '/dashboard/stores',
          name: 'stores',
          component: StoreView
        },
        {
          path: '/dashboard/warehouses',
          name: 'warehouses',
          component: WarehouseView
        },
        {
          path: '/dashboard/suppliers',
          name: 'suppliers',
          component: SupplierView
        },
        {
          path: '/dashboard/employees',
          name: 'employees',
          component: EmployeeView
        },
        {
          path: '/dashboard/settings',
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
  {
    path: '/signup/company',
    name: 'companySignup',
    component: CompanySignupView
  },
  {
    path: '/signup/admin',
    name: 'adminSignup',
    component: AdminSignupView,
    props: true
  },
  {
    path: '/login',
    name: 'signin',
    component: LoginView,
    props: true
  },
  {
    path: '/logout',
    name: 'logout',
    component: LoginView,
    props: true
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
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiredLogin) && !store.state.authenticated) {
    next ({name: 'sigin', query: {to: to.path}});
  }
  else
  {
  next();
  }
})
//
// router.beforeEach((to, from, next) => {
//   initializeAccount(store);
//   next();
// });
export default router
