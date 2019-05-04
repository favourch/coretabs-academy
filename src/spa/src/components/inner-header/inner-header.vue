<template>
<div class="inner-header">
  <v-toolbar class="white">
    <v-toolbar-side-icon v-if="!isProfile" v-on:click="$parent.$emit('toggle-drawer')"></v-toolbar-side-icon>
    <v-toolbar-title v-if="!isProfile" class="mx-auto">{{title}}</v-toolbar-title>
    <v-toolbar-title v-else class="mx-auto">الملف الشخصي</v-toolbar-title>
    <nav>
      <!--<router-link to="/">
        <img :src="$store.state.icon" alt="coretabs" />
      </router-link>-->
      <v-menu :close-on-content-click="false" v-model="menu" content-class="notifications-menu" offset-y>
        <v-btn slot="activator" class="menu" :class="{'unread': unread}" @click="set_unread">
          <img v-if="avatar_url" :src="avatar_url" />
          <span v-else v-html="avatar_letter"></span>
        </v-btn>
        <v-card>
          <v-list>
            <v-list-tile avatar>
              <!--
                <a :href="summary" target="_blank">
                <v-list-tile-avatar>
                  <img v-if="avatar_url" :src="avatar_url" />
                  <span v-else v-html="avatar_letter"></span>
                </v-list-tile-avatar>
                <v-list-tile-title v-html="$store.getters.user('name')"></v-list-tile-title>
              </a>
              -->
              <router-link :to="{name: 'profile', params: {username: $store.getters.user('username')}}">
                <v-list-tile-avatar>
                  <img v-if="avatar_url" :src="avatar_url" />
                  <span v-else v-html="avatar_letter"></span>
                </v-list-tile-avatar>
                <v-list-tile-title v-html="$store.getters.user('name')"></v-list-tile-title>
              </router-link>
            </v-list-tile>
          </v-list>
          <v-list v-if="notifications">
            <v-list-tile v-for="(notification, i) in notifications" :key="i" class="notification" :class="{'unread': !notification.read}">
              <v-list-tile-title>
                <a :href="`https://forums.coretabs.net/t/${notification.slug}/${notification.topic_id}${(notification.post_number > 1) ? '/' + notification.post_number : ''}`" @click="mark_read(notification)" target="_blank">
                  <v-icon>
                    {{ notification_icon(notification.notification_type) }}
                  </v-icon>
                  {{ notification.data.topic_title || notification.data.badge_name || 'System Notification' }}
                </a>
              </v-list-tile-title>
            </v-list-tile>
          </v-list>
          <v-card-actions>
            <router-link to="/profile" @click="menu=false">
              <v-icon>settings</v-icon>
              إعدادات الحساب
            </router-link>
            <router-link to="/logout" @click="menu=false">
              <v-icon>exit_to_app</v-icon> تسجيل خروج
            </router-link>
          </v-card-actions>
        </v-card>
      </v-menu>
    </nav>
  </v-toolbar>
</div>
</template>
<script src="./inner-header.js"></script>
<style src="./inner-header.scss" lang="scss"></style>
