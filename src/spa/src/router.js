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
import TracksComponent from './components/tracks/tracks.vue'
import LessonComponent from './components/lesson/lesson.vue'
import ModulesComponent from './components/modules/modules.vue'
import WorkshopComponent from './components/workshop/workshop.vue'
import NotFoundComponent from './components/not-found/not-found.vue'
import WorkshopsComponent from './components/workshops/workshops.vue'

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
      name: 'signup',
      path: '/signup',
      component: SignUpComponent,
      beforeEnter: (to, from, next) => {
         (!store.getters.isLogin) ? next(): next('/')
      }
   }, {
      name: 'congratulations',
      path: '/congratulations',
      component: CongratulationsComponent,
      props: true,
      beforeEnter: (to, from, next) => {
         (!store.getters.isLogin) ? next(): next('/')
      }
   }, {
      name: 'confirm-account',
      path: '/confirm-account/:key',
      component: ConfirmAccountComponent,
      beforeEnter: (to, from, next) => {
         (!store.getters.isLogin) ? next(): next('/')
      }
   }, {
      name: 'account-confirmed',
      path: '/account-confirmed',
      component: AccountConfirmedComponent,
      beforeEnter: (to, from, next) => {
         (store.getters.isLogin) ? next(): next('/')
      }
   }, {
      name: 'forgot-password',
      path: '/forgot-password',
      component: ForgotPasswordComponent,
      beforeEnter: (to, from, next) => {
         (!store.getters.isLogin) ? next(): next('/')
      }
   }, {
      name: 'reset-password',
      path: '/reset-password',
      component: ResetPasswordComponent,
      beforeEnter: (to, from, next) => {
         (!store.getters.isLogin) ? next(): next('/')
      }
   }, {
      name: 'signin',
      path: '/signin',
      component: SignInComponent,
      beforeEnter: (to, from, next) => {
         (!store.getters.isLogin) ? next(): next('/')
      }
   }, {
      name: 'select-track',
      path: '/select-track',
      component: SelectTrackComponent
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
      beforeEnter: (to, from, next) => {
         (store.getters.isLogin) ? next(): next('/')
      }
   }, {
      name: 'logout',
      path: '/logout',
      component: LogoutComponent,
      beforeEnter: (to, from, next) => {
         (store.getters.isLogin) ? next(): next('/')
      }
   }, {
      name: '404',
      path: '/404',
      component: NotFoundComponent
   }, {
      path: '*',
      redirect: '/404'
   }, {
      name: 'tracks',
      path: '/tracks',
      component: TracksComponent
   }, {
      name: 'workshops',
      path: '/tracks/:track',
      component: WorkshopsComponent,
      children: [{
         name: 'workshop',
         path: ':workshop',
         component: WorkshopComponent
      }],
      beforeEnter: (to, from, next) => {
         (store.getters.isLogin) ? next(): next('/')
      }
   }, {
      name: 'modules',
      component: ModulesComponent,
      path: '/tracks/:track/:workshop/:module',
      children: [{
         name: 'lessons',
         path: ':lesson',
         component: LessonComponent
      }],
      beforeEnter: (to, from, next) => {
         (store.getters.isLogin) ? next(): next('/')
      }
   }]
})

router.beforeEach(async (to, from, next) => {
   if (window.localStorage.getItem('token') && !store.getters.isLogin) {
      await Vue.prototype.$auth.checkUser(store)
   }
   next()
})

export default router
