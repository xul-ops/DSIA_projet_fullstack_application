import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
import './router/permission' // permission control
import '@/styles/common.scss'
import '@/styles/normalize.css'

// svg icon
import SvgIcon from '@/components/SvgIcon/SvgIcon.vue'// svg组件
Vue.component('svg-icon', SvgIcon)
const requireContext = require.context('./assets/icons', false, /\.svg$/)
requireContext.keys().forEach(requireContext)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
