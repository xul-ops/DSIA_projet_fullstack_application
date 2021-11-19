import router from './index'
import NProgress from 'nprogress' // progress bar
import { setDocumentTitle, domTitle } from '@/utils/domUtil'
import 'nprogress/nprogress.css'

router.beforeEach((to, from, next) => {
    NProgress.start() // start progress bar
    to.meta && typeof to.meta.title !== 'undefined' && setDocumentTitle(`${to.meta.title} - ${domTitle}`)
    // todo permission
    next()
})

router.afterEach(() => {
    NProgress.done() // finish progress bar
    document.querySelector('html').scrollTop = 0  //page back to top
})
