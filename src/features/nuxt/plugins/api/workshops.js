/* eslint-disable */
import Vue from 'vue'
import axios from 'axios'
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
  getWorkshopsData(url) {
    return axios.get(url)
      .then(response => {
        let workshops = []
        response.data.forEach((workshop, workshopIndex) => {
          workshops.push({
            index: workshopIndex + 1,
            url: {
              name: 'workshop',
              params: {
                workshop: workshop.slug
              }
            },
            level: workshop.level,
            title: workshop.title,
            duration: workshop.duration,
            description: workshop.description,
            shown_percentage: workshop.shown_percentage,
            workshop_result_url: workshop.workshop_result_url,
            used_technologies: workshop.used_technologies.split(', ').reverse(),
            last_update_date: Vue.prototype.$date.get(new Date(workshop.last_update_date)),
            authors: workshop.authors,
            modules: []
          })
          workshop.modules.forEach((module, moduleIndex) => {
            workshops[workshopIndex].modules.push({
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
              workshops[workshopIndex].modules[moduleIndex].lessons.push({
                index: lessonIndex + 1,
                url: {
                  name: 'lessons',
                  params: {
                    module: module.slug,
                    lesson: lesson.slug,
                    workshopURL: workshop.url,
                    modules: workshops[workshopIndex].modules
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
        })
        return workshops
      })
      .catch((err) => {
        return err
      })
  }
}

export default WorkshopsAPI
