/* eslint-disable */
import Vue from 'vue'
import router from '../router'

const WorkshopsAPI = {
  getWorkshopId(workshops) {
    let index = workshops.findIndex((workshop) => {
      return router.app.$route.params.workshop === workshop.url.params.workshop
    })
    if (index === -1) { router.push('/404') } else { return workshops[index] }
  },
  getModuleId(modules) {
    let index = modules.findIndex((module) => {
      return router.app.$route.params.module === module.url.params.module
    })
    return modules[index]
  },
  getLessonId(lessons) {
    let index = lessons.findIndex((module) => {
      return router.app.$route.params.lesson === module.url.params.lesson
    })
    if (index === -1) { router.push('/404') } else { return lessons[index] }
  },
  getWorkshops(url) {
    return axios.get(url, {
      withCredentials: true
    }).then(async (response) => {
      let data = await response.data
      let workshops = []
      for (let workshopIndex = 0; workshopIndex < data.length; workshopIndex++) {
        let workshop = {
          index: workshopIndex + 1,
          url: {
            name: 'workshop',
            params: {
              workshop: data[workshopIndex].slug
            }
          },
          title: data[workshopIndex].title,
          shown_percentage: data[workshopIndex].shown_percentage
        }
        workshops.push(workshop)
      }
      return workshops
    })
    .catch(err => {
      console.error(err)
    })
  },
  async getWorkshop(url) {
    return axios.get(url, {
      withCredentials: true
    }).then(response => {
      let workshop = {
        url: {
          name: 'workshop',
          params: {
            workshop: response.data.slug
          }
        },
        title: response.data.title,
        shown_percentage: response.data.shown_percentage,
        level: response.data.level,
        duration: response.data.duration,
        description: response.data.description,
        workshop_result_url: response.data.workshop_result_url,
        workshop_forums_url: response.data.workshop_forums_url,
        used_technologies: [],
        last_update_date: Vue.prototype.$date.get(new Date(response.data.last_update_date)),
        authors: response.data.authors,
        modules: []
      }
      if (response.data.used_technologies.length > 0) {
        workshop.used_technologies = response.data.used_technologies.split(', ').reverse()
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
          workshop.modules[moduleIndex].lessons.push({
            index: lessonIndex + 1,
            url: {
              name: 'lessons',
              params: {
                module: module.slug,
                lesson: lesson.slug,
                modules: workshop.modules,
                _workshop: {
                  title: workshop.title,
                  forums: workshop.workshop_forums_url
                }
              }
            },
            title: lesson.title,
            type: lesson.type,
            video: (lesson.video_url) ? lesson.video_url : undefined,
            markdown: lesson.markdown_url,
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
