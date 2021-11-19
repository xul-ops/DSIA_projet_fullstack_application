import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/user/Login.vue'
import Layout from "@/components/Layout/Layout";
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login,
    meta:{
      title:'Login'
    }
  },
  {
    path: '/movie',
    component: Layout,
    children:[{
      path: 'list',
      name: 'Home',
      component: ()=>import('@/views/movie/List.vue'),
      meta:{
        title:'Home'
      }
    },{
      path: 'search',
      name: 'Search',
      component: ()=>import('@/views/movie/Search.vue'),
      meta:{
        title:'Search'
      }
    },{
      path: 'detail',
      name: 'Detail',
      component: ()=>import('@/views/movie/Detail.vue'),
      meta:{
        title:'Detail'
      }
    }]
  },
]

const router = new VueRouter({
  routes
})

export default router
