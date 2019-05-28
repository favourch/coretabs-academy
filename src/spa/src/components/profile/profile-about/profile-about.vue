<template>
  <div v-if="loaded" class="about">

    <v-card class="elevation-0">
      <v-container class="no-select" fluid>
        <v-layout row wrap>
          <v-flex xs12 sm12 md8>

            <div class="about-item">
              <h2 class="about-item__title">نبذة عني</h2>
              <p class="user-bio">
                {{ bio }}
              </p>

            </div>

            <div class="about-item" v-if="profile.skills.length > 0">
              <h2 class="about-item__title">المهارات البرمجية</h2>

              <div class="lang-items">
                <div class="lang-item" v-for="(skill, index) in profile.skills" :key="index">
                  <div class="lang-img-wrapper">{{ skill.value }}</div>
                  <span class="lang-title">{{ skill.text }}</span>
                </div>
              </div>
            </div>
          </v-flex>
          <v-flex xs12 sm12 md4 v-if="profile.date_joined">
            <section class="other-info">
              <div class="about-item">
                <h4 class="about-item__title">تاريخ الإنضمام</h4>
                <span>
                  {{ profile.date_joined }}
                </span>
              </div>

              <ul class="links info-item" v-if="links.length > 0">
                <li v-for="(link, i) in links" :key="i" class="links__item icon">
                  <a :href="link.url" :title="link.name" target="_blank"></a>
                  <i :class="`icon-${link.name}`"></i>
                </li>
              </ul>

            </section>

          </v-flex>
        </v-layout>
      </v-container>
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

<script src="./profile-about.js"></script>
<style src="./profile-about.scss" lang="scss" scoped></style>
