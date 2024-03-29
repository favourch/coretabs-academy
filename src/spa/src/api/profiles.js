/* eslint-disable */
import Vue from 'vue'
import { createRouter } from '../router'
import Cookies from 'js-cookie'

const router = createRouter()

const ProfilesAPI = {
  getProfileId(profiles) {
    let index = profiles.findIndex((profile) => {
      return router.app.$route.params.profile === profile.url.params.profile
    })
    if (index === -1) { router.push('/404') } else { return profiles[index] }
  },
  getProfiles(url) {
    return axios.get(url, {
      withCredentials: true
    }).then(async (response) => {
      let data = await response.data
      let profiles = []
      for (let profileIndex = 0; profileIndex < data.length; profileIndex++) {
        let profile = {
          index: profileIndex + 1,
          url: {
            name: 'profile',
            params: {
              profile: data[profileIndex].slug
            }
          },
          title: data[profileIndex].title
        }
        profiles.push(profile)
      }
      return profiles
    })
    .catch(err => {
      console.error(err)
    })
  },
  getProfile(url) {
    return axios.get(url, {
      withCredentials: true
    }).then(response => {
      let profile = {
        url: {
          name: 'profile',
          params: {
            profile: response.data.username
          }
        },
        username: response.data.username,
        name: response.data.name,
        country: response.data.country,
        date_joined: Vue.prototype.$date.get(new Date(response.data.date_joined)),
        role: response.data.role,
        level: response.data.level,
        description: response.data.description,
        bio: response.data.bio,
        avatar_url: response.data.avatar_url,
        github_link: response.data.github_link,
        facebook_link: response.data.facebook_link,
        twitter_link: response.data.twitter_link,
        linkedin_link: response.data.linkedin_link,
        website_link: response.data.website_link,
        skills: response.data.skills,
        certificates: [],
        projects: response.data.projects
      }
      /*if (response.data.languages.length > 0) {
        profile.languages = response.data.languages.split(', ').reverse()
      }*/
      response.data.certificates.forEach((certificate, certificateIndex) => {
        profile.certificates.push({
          id: certificate.id,
          date: Vue.prototype.$date.get(new Date(certificate.date)),
          heading: certificate.heading,
          index: certificateIndex + 1,
          /*url: {
            name: 'certificates'
          }*/
        })
      })
      return profile;
    })
    .catch(err => {
      console.error(err)
    })
  },
  async getCurrentProfile(url) {
    return axios.get(url, {
      withCredentials: true
    }).then(response => {
      let profile = {
        /*url: {
          name: 'profile',
          params: {
            profile: response.data.slug
          }
        },*/
        username: response.data.username,
        name: response.data.name,
        role: response.data.role,
        level: response.data.level,
        description: response.data.description,
        bio: response.data.bio,
        avatar_url: response.data.avatar_url,
        github_link: response.data.github_link,
        facebook_link: response.data.facebook_link,
        twitter_link: response.data.twitter_link,
        linkedin_link: response.data.linkedin_link,
        website_link: response.data.website_link,
        skills: response.data.skills,
        certificates: []
      }
      /*if (response.data.languages.length > 0) {
        profile.languages = response.data.languages.split(', ').reverse()
      }*/
      response.data.certificates.forEach((certificate, certificateIndex) => {
        profile.certificates.push({
          id: certificate.id,
          date: Vue.prototype.$date.get(new Date(certificate.date)),
          heading: certificate.heading,
          index: certificateIndex + 1,
          /*url: {
            name: 'certificates',
            params: {
              certificate: certificate.slug
            }
          }*/
        })
      })
      return profile;
    })
    .catch(err => {
      console.error(err)
    })
  },
  getCertificate(url) {
    return axios.get(url, {
      withCredentials: true
    }).then(response => {
      let certificate = {
        /*url: {
          name: 'certificate',
          params: {
            certificate: response.data.id
          }
        },*/
        full_name: response.data.full_name,
        date: response.data.date,
        heading: response.data.heading,
        body: response.data.body,
        signature: response.data.signature,
      }
      return certificate;
    })
    .catch(err => {
      console.error(err)
    })
  },
  async createProject(root) {
    root.alert.success = false
    root.alert.error = false

    let formData = new FormData()
    formData.append('description', root.project_name)
    formData.append('github_link', root.repo_link)
    formData.append('live_demo_link', root.demo_link)
    formData.append('photo', root.validImage.imageData)

    return await axios.post(`/api/v1/profile/projects`, formData, {
      withCredentials: true,
      headers: {
        'X-CSRFToken': Cookies.get('csrftoken'),
        'Content-Type': 'multipart/form-data'
      }
    }).then((response) => {
      root.alert.success = true
      root.alert.message = root.i18n.add_success_message
      
      return false
    }).catch((error) => {
      if (error.response) {
        root.alert.error = true
        if (error.response.status === 400) {
          for (var err in error.response.data) {
            root.alert.message = error.response.data[err][0]
            break
          }
        } else {
          root.alert.message = root.form.message_endpoint_error
        }
        return false
      }
    })
  },
  async changeProjectInfo(root) {
    root.alert.success = false
    root.alert.error = false
    let id = root.editProjectId;

    let formData = new FormData()
    formData.append('description', root.project_name)
    formData.append('github_link', root.repo_link)
    formData.append('live_demo_link', root.demo_link)
    formData.append('photo', root.validImage.imageData)

    return await axios.patch(`/api/v1/profile/projects/${id}`, formData, {
      withCredentials: true,
      headers: {
        'X-CSRFToken': Cookies.get('csrftoken'),
        'Content-Type': 'multipart/form-data'
      }
    }).then((response) => {
      root.alert.success = true
      root.alert.message = root.i18n.edit_success_message

      return false
    }).catch((error) => {
      if (error.response) {
        root.alert.error = true
        if (error.response.status === 400) {
          for (var err in error.response.data) {
            root.alert.message = error.response.data[err][0]
            break
          }
        } else {
          root.alert.message = root.form.message_endpoint_error
        }
        return false
      }
    })
  },
  async deleteProject(root) {
    root.alert.success = false
    root.alert.error = false
    let id = root.editProjectId;

    return await axios.delete(`/api/v1/profile/projects/${id}`, {
      withCredentials: true,
      headers: {
        'X-CSRFToken': Cookies.get('csrftoken'),
        'Content-Type': 'multipart/form-data'
      }
    }).then((response) => {
      root.alert.success = true

      return false;
    }).catch((error) => {
      if (error.response) {
        root.alert.error = true
        if (error.response.status === 400) {
          for (var err in error.response.data) {
            root.alert.message = error.response.data[err][0]
            break
          }
        } else {
          root.alert.message = root.form.message_endpoint_error
        }
        return false
      }
    })
  }
}

export default ProfilesAPI
