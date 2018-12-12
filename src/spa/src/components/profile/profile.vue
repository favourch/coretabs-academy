<template>
  <div class="profile">
    <inner-header-component></inner-header-component>

    <v-container fluid class="pa-0" fill-height>
      <v-layout :column="$vuetify.breakpoint.smAndDown">
        <v-flex xs12 md3 class="profile">
          <div class="profile-header">
            
            <v-avatar size="150" color="grey lighten-4">
              
              <div class="user-badge">
                <span class="icon"></span>
              </div>

              <img src="https://via.placeholder.com/150" alt="user">
            </v-avatar>

            <h2 class="mt-4 mb-2 profile-username profile-badge profile-badge-verified">أيمن الرفاعي</h2>

            <h3 class="profile-subheading">مطور واجهات ويب</h3>

            <div class="my-4 user-level">مستوى متوسط</div>

            <div class="profile-location">
              <v-icon right small>place</v-icon>
              <span class="profile-location-title">ليبيا - الخمس</span>
            </div>
          </div>

          <v-list>
            <v-divider></v-divider>

            <v-subheader class="profile-subheader">المهارات المفضلة</v-subheader>

            <v-list-tile>
              <v-chip small label outline v-for="n in 3">Tag {{ n }}</v-chip>
            </v-list-tile>
          </v-list>
        </v-flex>

        <v-flex xs12 md9>
          <v-tabs>
            <v-tab v-for="tab in tabs" :key="tab.name" ripple :to="tab.path">{{ tab.text }}</v-tab>
          </v-tabs>
          <router-view></router-view>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>


<script src="./profile.js"></script> 
<style src="./profile.scss" lang="scss"></style> 
