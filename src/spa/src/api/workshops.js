/* eslint-disable */
import Vue from 'vue'
import router from '../router'

const WorkshopsAPI = {
   getWorkshopId(workshops) {
      let index = workshops.findIndex(function(workshop) {
         return router.app.$route.params.workshop === workshop.url.params.workshop
      })
      if (index === -1) {
         router.push('/404')
      } else {
         return workshops[index]
      }
   },
   getModuleId(modules) {
      let index = modules.findIndex(function(module) {
         return router.app.$route.params.module === module.url.params.module
      })
      return modules[index]
   },
   getLessonId(lessons) {
      let index = lessons.findIndex(function(module) {
         return router.app.$route.params.lesson === module.url.params.lesson
      })
      if (index === -1) {
         router.push('/404')
      } else {
         return lessons[index]
      }
   },
   navigationToFirstWorkshop(url) {
      axios.get(url)
         .then(response => {
            router.push({
               name: 'workshop',
               params: {
                  workshop: response.data.workshops[0]
               }
            })
         })
         .catch(err => {
            console.error(err)
         })
   },
   getWorkshopsList(url) {
      return axios.get(url)
         .then(async (response) => {
            let workshops = []
            for (let workshopIndex = 0; workshopIndex < response.data.workshops.length; workshopIndex++) {
               let workshop = await Vue.prototype.$api.getWorkshopData(`/api/v1/tracks/${router.app.$route.params.track}/workshops/${response.data.workshops[workshopIndex]}`)
               workshop.index = workshopIndex + 1
               workshops.push(workshop)
            }
            return workshops
         })
         .catch(err => {
            console.error(err)
         })
   },
   async getWorkshopData(url) {
      return axios.get(url)
         .then(response => {
            let workshop = {
               index: 0,
               url: {
                  name: 'workshop',
                  params: {
                     workshop: response.data.slug
                  }
               },
               level: response.data.level,
               title: response.data.title,
               duration: response.data.duration,
               description: response.data.description,
               shown_percentage: response.data.shown_percentage,
               workshop_result_url: response.data.workshop_result_url,
               workshop_forums_url: response.data.workshop_forums_url,
               used_technologies: response.data.used_technologies.split(', ').reverse(),
               last_update_date: Vue.prototype.$date.get(new Date(response.data.last_update_date)),
               authors: response.data.authors,
               modules: []
            }
            response.data.modules.forEach((module, moduleIndex) => {
               workshop.modules.push({
                  active: true,
                  title: module.title,
                  index: moduleIndex + 1,
                  url: {
                     name: 'modules',
                     params: {
                        module: module.slug
                     }
                  },
                  lessons: []
               })
               module.lessons.forEach((lesson, lessonIndex) => {
                  let url = ''
                  let notes = ''
                  if (lesson.type === '0' || lesson.type === '1') {
                     url = Vue.prototype.$encryption.b64EncodeUnicode(lesson.video_url)
                     notes = Vue.prototype.$encryption.b64EncodeUnicode(lesson.markdown_url)
                  } else {
                     url = Vue.prototype.$encryption.b64EncodeUnicode(lesson.markdown_url)
                     notes = ''
                  }
                  workshop.modules[moduleIndex].lessons.push({
                     index: lessonIndex + 1,
                     url: {
                        name: 'lessons',
                        params: {
                           module: module.slug,
                           lesson: lesson.slug,
                           workshopURL: response.data.url,
                           modules: workshop.modules
                        },
                        query: {
                           url: url,
                           notes: notes,
                           type: Vue.prototype.$encryption.b64EncodeUnicode(lesson.type)
                        }
                     },
                     query: {
                        url: url,
                        notes: notes,
                        type: Vue.prototype.$encryption.b64EncodeUnicode(lesson.type)
                     },
                     type: lesson.type,
                     title: lesson.title,
                     is_shown: lesson.is_shown
                  })
               })
            })
            return workshop
         })
         .catch(err => {
            console.error(err)
         })
   }
}

export default WorkshopsAPI
