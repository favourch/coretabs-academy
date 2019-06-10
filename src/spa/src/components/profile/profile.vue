<template>
  <div v-if="loaded" id="profile">
    <NavigatorDrawerComponent />
    <section id="column-flexed">
      <inner-header-component></inner-header-component>
      <v-container fluid class="pa-0">
        <v-layout :column="$vuetify.breakpoint.smAndDown">
          <v-flex xs12 md3 class="profile">
            <div class="profile-header">
              <v-avatar size="150" color="grey lighten-4">
                <div class="user-badge" v-if="profile.role && profile.role !== 'Student'">
                  <span class="icon"></span>
                </div>
                <div class="edit-image-btn" title="تغيير الصورة الشخصية" v-if="showEditProfileBtn">
                  <v-btn depressed fab to="/profile/personal-info"><v-icon>photo_camera</v-icon></v-btn>
                </div>
                <img v-if="avatar_url" :src="avatar_url" :alt="profile.name">
                <span v-else v-html="avatar_letter"></span>
              </v-avatar>

              <h2 class="mt-4 mb-2 profile-username" :class="{'profile-badge profile-badge-verified': profile.role && profile.role !== 'Student'}">{{ profile.name }}</h2>
              <h3 class="profile-subheading" v-if="profile.description">{{ profile.description }}</h3>
              <!-- <div class="my-4 user-level" v-if="profile.level">{{ profile.level }}</div> -->
              <div class="profile-location" v-if="profile.country">
                <v-icon right small>place</v-icon>
                <span class="profile-location-title">{{ profile.country.text }}</span>
              </div>
              <div class="edit-profile-btn" v-if="showEditProfileBtn">
                <v-btn round dark depressed class="mt-5" to="/profile/profile-info/">عدل ملفك الشخصي</v-btn>
              </div>

            </div>

            <!-- <v-list>
              <v-divider></v-divider>
              <v-subheader class="profile-subheader">المهارات المفضلة</v-subheader>
              <v-list-tile>
                <v-chip small label outline v-for="n in 3" :key="n">Tag {{ n }}</v-chip>
              </v-list-tile>
            </v-list> -->
          </v-flex>

          <v-flex xs12>
            <v-tabs>
              <v-tab v-for="tab in tabs" :key="tab.name" ripple :to="{name: tab.name}">{{ tab.text }}</v-tab>
            </v-tabs>
            <div class="profile-sub-page">
              <router-view></router-view>
            </div>

            <JoinInviteComponent v-if="!$store.getters.isLogin" />
          </v-flex>
        </v-layout>
      </v-container>
    </section>
  </div>

  <div v-else class="progress-container">
    <v-container fluid fill-height>
      <v-layout column align-center justify-center>
        <v-progress-circular indeterminate :size="$store.state.progress.size" :width="$store.state.progress.width" v-if="!$store.state.progress.error"></v-progress-circular>
        <div class="error text-center" v-else>!</div>
        <div class="text text-center">{{$store.state.progress.text}}</div>
      </v-layout>
    </v-container>
  </div>
</template>

<script src="./profile.js"></script>
<style src="./profile.scss" lang="scss"></style>
