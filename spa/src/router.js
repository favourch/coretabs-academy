import Vue from 'vue'
import Router from 'vue-router'
import HomeComponent from './components/home/home.vue'
import NotReadyComponent from './components/not-ready/not-ready.vue'
import AboutComponent from './components/about/about.vue'
import ContactUsComponent from './components/contact-us/contact-us.vue'
import PageComponent from './components/page/page.vue'
import SignUpComponent from './components/signup/signup.vue'
import CongratulationsComponent from './components/congratulations/congratulations.vue'
import AccountConfirmedComponent from './components/account-confirmed/account-confirmed.vue'
import ResetPasswordComponent from './components/reset-password/reset-password.vue'
import ForgotPasswordComponent from './components/forgot-password/forgot-password.vue'
import SignInComponent from './components/signin/signin.vue'
import SelectTrackComponent from './components/select-track/select-track.vue'
import TracksComponent from './components/tracks/tracks.vue'
import LessonComponent from './components/lesson/lesson.vue'
import ModulesComponent from './components/modules/modules.vue'
import WorkshopComponent from './components/workshop/workshop.vue'
import NotFoundComponent from './components/not-found/not-found.vue'
import WorkshopsComponent from './components/workshops/workshops.vue'

Vue.use(Router)

export default new Router({
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
    component: SignUpComponent
  }, {
    name: 'congratulations',
    path: '/congratulations',
    component: CongratulationsComponent
  }, {
    name: 'account-confirmed',
    path: '/account-confirmed',
    component: AccountConfirmedComponent
  }, {
    name: 'reset-password',
    path: '/reset-password',
    component: ResetPasswordComponent
  }, {
    name: 'forgot-password',
    path: '/forgot-password',
    component: ForgotPasswordComponent
  }, {
    name: 'signin',
    path: '/signin',
    component: SignInComponent
  }, {
    name: 'select-track',
    path: '/select-track',
    component: SelectTrackComponent
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
    path: '/:track',
    component: WorkshopsComponent,
    children: [{
        name: 'workshop',
        path: ':workshop',
        component: WorkshopComponent
    }]
  }, {
    name: 'modules',
    component: ModulesComponent,
    path: '/:track/:workshop/:module',
    children: [{
        name: 'lessons',
        path: ':lesson',
        component: LessonComponent
    }]
  }]
})
