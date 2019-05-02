import Vue from 'vue'
import Router from 'vue-router'
import store from './store/app.store'
import HomeComponent from './components/home/home.vue'
import NotReadyComponent from './components/not-ready/not-ready.vue'
import AboutComponent from './components/about/about.vue'
import ContactUsComponent from './components/contact-us/contact-us.vue'
import PageComponent from './components/page/page.vue'
import SignUpComponent from './components/signup/signup.vue'
import CongratulationsComponent from './components/congratulations/congratulations.vue'
import ConfirmAccountComponent from './components/confirm-account/confirm-account.vue'
import ApplicationSubmitted from './components/application-submitted/application-submitted.vue'
import BatchNotStarted from './components/batch-not-started/batch-not-started.vue'
import AccountConfirmedComponent from './components/account-confirmed/account-confirmed.vue'
import ResetPasswordComponent from './components/reset-password/reset-password.vue'
import ForgotPasswordComponent from './components/forgot-password/forgot-password.vue'
import SignInComponent from './components/signin/signin.vue'
import SelectTrackComponent from './components/select-track/select-track.vue'
import ProfileSettingsComponent from './components/profile-settings/profile-settings.vue'
import EditPersonalInfoComponent from './components/profile-settings/edit-personal-info/edit-personal-info.vue'
import ChangeTrackComponent from './components/profile-settings/change-track/change-track.vue'
import ChangePasswordComponent from './components/profile-settings/change-password/change-password.vue'
import LogoutComponent from './components/logout/logout.vue'
import LessonComponent from './components/lesson/lesson.vue'
import ModulesComponent from './components/modules/modules.vue'
import WorkshopComponent from './components/workshop/workshop.vue'
import NotFoundComponent from './components/not-found/not-found.vue'
import WorkshopsComponent from './components/workshops/workshops.vue'
import maintenanceComponent from './components/maintenance/maintenance.vue'
import ProfileComponent from './components/profile/profile.vue'
import ProfileAboutComponent from './components/profile/profile-about/profile-about.vue'
import ProfileCertificatesComponent from './components/profile/profile-certificates/profile-certificates.vue'
import TracksComponent from './components/tracks/tracks.vue'
import FrontendTrackComponent from './components/frontend-track/frontend-track.vue'
import CertificateComponent from './components/certificate/certificate.vue'

import i18n from './i18n/ar/i18n'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [{
    path: '/',
    name: 'home',
    component: HomeComponent
  }, {
    path: '/home',
    redirect: '/'
  }, {
    name: 'not-ready',
    path: '/not-ready',
    component: NotReadyComponent
  }, {
    name: 'about',
    path: '/about',
    component: AboutComponent
  }, {
    name: 'contact-us',
    path: '/contact-us',
    component: ContactUsComponent
  }, {
    name: 'page',
    path: '/page/:page',
    component: PageComponent
  }, {
    name: 'tracks',
    path: '/tracks',
    component: TracksComponent
  }, {
    name: 'frontend-track',
    path: '/tracks/frontend',
    component: FrontendTrackComponent
  }, {
    name: 'signup',
    path: '/signup',
    component: SignUpComponent,
    beforeEnter: (to, from, next) => { (!store.getters.isLogin) ? next() : next('/') }
  }, {
    name: 'congratulations',
    path: '/congratulations',
    component: CongratulationsComponent,
    props: true,
    beforeEnter: (to, from, next) => { (!store.getters.isLogin) ? next() : next('/') }
  }, {
    name: 'confirm-account',
    path: '/confirm-account/:uid/:key',
    component: ConfirmAccountComponent
  }, {
    name: 'application-submitted',
    path: '/application-submitted',
    component: ApplicationSubmitted,
    beforeEnter: (to, from, next) => { (!store.getters.isLogin) ? next() : next('/') }
  }, {
    name: 'batch-not-started',
    path: '/batch-not-started',
    component: BatchNotStarted
  }, {
    name: 'account-confirmed',
    path: '/account-confirmed',
    component: AccountConfirmedComponent,
    beforeEnter: (to, from, next) => { (store.getters.isLogin) ? next() : next('/') }
  }, {
    name: 'forgot-password',
    path: '/forgot-password',
    component: ForgotPasswordComponent,
    beforeEnter: (to, from, next) => { (!store.getters.isLogin) ? next() : next('/') }
  }, {
    name: 'reset-password',
    path: '/reset-password/:uid/:key',
    component: ResetPasswordComponent,
    beforeEnter: (to, from, next) => { (!store.getters.isLogin) ? next() : next('/') }
  }, {
    name: 'signin',
    path: '/signin',
    component: SignInComponent,
    beforeEnter: (to, from, next) => { (!store.getters.isLogin) ? next() : next('/') }
  }, {
    name: 'profile',
    path: '/:username',
    component: ProfileComponent,
    redirect: '/:username/about',
    children: [{
      name: 'profile-about',
      path: 'about',
      component: ProfileAboutComponent
    },
    {
      name: 'profile-certificates',
      path: 'certificates',
      component: ProfileCertificatesComponent
    }]
    // beforeEnter: (to, from, next) => { (store.getters.isLogin) ? next() : next('/') }
  }, {
    name: 'select-track',
    path: '/select-track',
    component: SelectTrackComponent,
    beforeEnter: (to, from, next) => {
      (store.getters.isLogin && (!store.getters.account('track') || (store.getters.account('track') === 'tour'))) ? next() : next('/')
    }
  }, {
    path: '/profile',
    component: ProfileSettingsComponent,
    children: [{
      path: '',
      redirect: {
        name: 'personal-info'
      }
    }, {
      name: 'personal-info',
      path: '/profile/personal-info',
      component: EditPersonalInfoComponent
    }, {
      name: 'change-track',
      path: '/profile/change-track',
      component: ChangeTrackComponent
    }, {
      name: 'change-password',
      path: '/profile/change-password',
      component: ChangePasswordComponent
    }],
    beforeEnter: (to, from, next) => { (store.getters.isLogin) ? next() : next('/') }
  }, {
    name: 'logout',
    path: '/logout',
    component: LogoutComponent,
    beforeEnter: (to, from, next) => { (store.getters.isLogin) ? next() : next('/') }
  }, {
    name: '404',
    path: '/404',
    component: NotFoundComponent
  },
  {
    name: 'maintenance',
    path: '/maintenance',
    component: maintenanceComponent
  }, {
    path: '*',
    redirect: '/404'
  }, {
    name: 'workshops',
    path: '/classroom/:track',
    component: WorkshopsComponent,
    children: [{
      name: 'workshop',
      path: ':workshop',
      component: WorkshopComponent
    }],
    beforeEnter: (to, from, next) => { (store.getters.isLogin) ? (store.getters.user('batch_status') ? next() : location.reload()) : next('/') }
  }, {
    name: 'modules',
    component: ModulesComponent,
    path: '/classroom/:track/:workshop/:module',
    children: [{
      name: 'lessons',
      path: ':lesson',
      component: LessonComponent
    }],
    beforeEnter: (to, from, next) => { (store.getters.isLogin) ? next() : next('/') }
  }, {
    name: 'certificate',
    component: CertificateComponent,
    path: '/certificate/:certificateId',
    props: true
  }]
})

router.beforeEach(async(to, from, next) => {
  if (typeof window !== 'undefined') {
    if (window.localStorage.getItem('token') && !store.getters.isLogin) {
      await Vue.prototype.$auth.checkUser(store)
    }
  }

  if (typeof document !== 'undefined') {
    const pageName = to.name
    if (i18n.meta[pageName]) {
      to.meta.title = i18n.meta[pageName].title + ' - ' + i18n.meta.default.title
    } else {
      to.meta.title = i18n.meta.default.title
    }
    document.title = to.meta.title
  }

  let isNotMaintenancePath = to.path !== '/maintenance'
  let isMaintenanceMode = process.env.MAINTENANCE_MODE === 'true' && store.state.maintenance
  if (isMaintenanceMode && isNotMaintenancePath) {
    if (to.query.maintenance === 'false') {
      store.state.maintenance = false
      next()
    } else {
      next('/maintenance')
    }
  } else {
    next()
  }
})

export function createRouter() {
  return router
}
