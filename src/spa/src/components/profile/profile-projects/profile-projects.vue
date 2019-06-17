<template>
<div v-if="loaded && projects && projects.length > 0" class="profile-projects">

  <div class="card-grid">

    <v-card class="project-card" v-for="(project,i) in projects" :key="i">
      <div class="card-pic">
        <img
          :src="project.photo"
        >
      </div>
      
      <v-card-title>
        <h3 class="card-title">{{project.description}}</h3>
      </v-card-title>

      <v-divider></v-divider>
        <v-card-actions class="pa-3">
          <a v-if="project.github_link" :href="'//' + project.github_link" target="_blank" class="download-btn">
            <i class="icon-github"></i>
            المستودع
          </a>
          <v-spacer></v-spacer>
          <a v-if="project.live_demo_link" :href="'//' + project.live_demo_link" target="_blank" class="download-btn">
            <v-icon class="card-icon">visibility</v-icon>
            معاينة
          </a>
        </v-card-actions>

    </v-card>

    <v-card class="add-card" :to="{name: 'manage-projects', params: {isAddFromRoute: true}}" v-if="$store.getters.user('username') === $route.params.username">
      <v-icon large class="card-icon">add</v-icon>
    </v-card>

  </div>
</div>
<div v-else-if="loaded && projects && projects.length === 0">
  <v-container fluid fill-height>
    <v-layout column align-center justify-center>
      <p>أعمل على رفع أول مشروع لي 💪</p>
      <div class="add-project-btn" v-if="$store.getters.user('username') === $route.params.username">
        <v-btn round dark depressed class="mt-5" :to="{name: 'manage-projects', params: {isAddFromRoute: true}}">أضف مشروعاً</v-btn>
      </div>
    </v-layout>
  </v-container>
</div>
<div v-else class="progress-container contrast">
  <v-container fluid fill-height>
    <v-layout column align-center justify-center>
      <v-progress-circular indeterminate :size="$store.state.progress.size" :width="$store.state.progress.width" v-if="!$store.state.progress.error"></v-progress-circular>
      <div class="error text-center" v-else>!</div>
      <div class="text text-center">{{$store.state.progress.text}}</div>
    </v-layout>
  </v-container>
</div>
</template>

<script src="./profile-projects.js"></script>

<style src="./profile-projects.scss" lang="scss"></style>
