<template>
<div v-if="loaded" class="workshop">
  <v-card class="elevation-0">
    <v-container class="no-select" fluid grid-list-xl>
      <v-layout row wrap align-center justify-center>
        <v-flex xs8 sm4 md3 v-if="workshop.level">
          <v-layout row wrap align-center justify-center>
            <img v-if="workshop.level === 'beginner'" src="../../assets/multimedia/icons/workshop/level1.svg" alt="course level icon">
            <img v-if="workshop.level === 'intermediate'" src="../../assets/multimedia/icons/workshop/level2.svg" alt="course level icon">
            <img v-if="workshop.level === 'advanced'" src="../../assets/multimedia/icons/workshop/level3.svg" alt="course level icon">
            <div class="text">
              <div v-html="i18n.card1.level.title"></div>
              <div v-html="i18n.card1.level.value[workshop.level]"></div>
            </div>
          </v-layout>
        </v-flex>
        <v-flex xs8 sm4 md3 v-if="workshop.duration">
          <v-layout row wrap align-center justify-center>
            <img src="../../assets/multimedia/icons/workshop/duration.svg" alt="duration icon">
            <div class="text">
              <div v-html="i18n.card1.duration.title"></div>
              <div v-html="`${workshop.duration} ${this.durationUnit}`"></div>
            </div>
          </v-layout>
        </v-flex>
        <v-flex xs8 sm4 md3 v-if="workshop.last_update_date">
          <v-layout row wrap align-center justify-center>
            <img src="../../assets/multimedia/icons/workshop/last-update.svg" alt="last update icon">
            <div class="text">
              <div v-html="i18n.card1.last_update_date"></div>
              <div>{{workshop.last_update_date}}</div>
            </div>
          </v-layout>
        </v-flex>
        <v-flex xs8 sm4 md3>
          <v-layout row wrap align-center justify-center>
            <v-flex md8>
              <v-btn round class="white--text" v-if="workshop.shown_percentage === 0" v-html="i18n.card1.start" :to="workshop.modules[0].lessons[0].url"></v-btn>
              <v-btn round class="white--text" v-else v-html="i18n.card1.continue" @click="getContinueURL(workshop)"></v-btn>
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-container>
  </v-card>
  <v-card class="elevation-0">
    <v-container class="no-select" fluid>
      <v-layout row wrap>
        <v-flex xs12 sm12 md7>
          <div class="title" v-if="workshop.description" v-html="i18n.card2.description"></div>
          <p v-if="workshop.description">{{workshop.description}}</p>
          <div class="title" v-if="workshop.used_technologies && workshop.used_technologies.length > 0" v-html="i18n.card2.used_technologies"></div>
          <div class="chips" v-if="workshop.used_technologies && workshop.used_technologies.length > 0">
            <div v-for="used_technologies in workshop.used_technologies" :key="used_technologies">
              <v-chip div v-for="technology in used_technologies.split(',')" :key="technology">{{technology}}</v-chip>
            </div>
          </div>
          <div class="title" v-html="i18n.card2.authors" v-if="workshop.authors && workshop.authors.length > 0"></div>
          <div class="authors" v-if="workshop.authors && workshop.authors.length > 0">
            <div class="author" v-for="(author, index) in workshop.authors" :key="index">
              <v-avatar>
                <img :src="getAuthorAvatar(author.avatar_url)" />
              </v-avatar>
              <div class="info">
                <div>
                  {{ author.name }}
                </div>
                <div>
                  {{ author.role }}
                </div>
              </div>
            </div>
          </div>
          <div class="title" v-html="i18n.card2.result" v-if="workshop.workshop_result_url"></div>
          <v-btn flat round target="_blank" v-if="workshop.workshop_result_url" :href="workshop.workshop_result_url" v-html="i18n.card2.resultBtn"></v-btn>
        </v-flex>
        <v-flex xs12 sm12 md5>
          <div class="navigation">
            <v-toolbar flat>
              <div class="progress">
                <div id="progress-bar" :style="{ width: progressValue + '%' }" :data-value="progressValue + '%'">
                </div>
              </div>
            </v-toolbar>
            <modules-nav-component v-if="workshop.modules" :modules="workshop.modules"></modules-nav-component>
          </div>
        </v-flex>
      </v-layout>
    </v-container>
  </v-card>
  <v-card class="elevation-0" v-if="workshop.workshop_forums_url">
    <a :href="workshop.workshop_forums_url" target="_blank">
    <v-container class="no-select" fluid grid-list-xl>
      <v-layout row wrap align-center justify-center>
        <v-flex xs11 sm11 md11>
          <v-layout row align-center>
            <img :src="$store.state.forumLogo" alt="forum-logo icon">
            <div class="text">
              <div v-html="i18n.card3.title"></div>
              <div>{{i18n.card3.text}} <span class="link-decoration">{{i18n.card3.here}}</span></div>
            </div>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-container>
     </a>
  </v-card>
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
<script src="./workshop.js"></script>
<style src="./workshop.scss" lang="scss"></style>
