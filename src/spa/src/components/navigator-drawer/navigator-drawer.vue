<template>
  <v-navigation-drawer v-model="drawer.isOpen" :right="drawer.isRight" :mini-variant.sync="mini" :width="200" hide-overlay app @mouseover.native="toggleDrawer($event)" @mouseleave.native="toggleDrawer($event)">
    <v-toolbar flat class="transparent">
      <v-list class="pa-0">
        <v-list-tile avatar>
          <v-list-tile-avatar v-if="mini">
            <img :src="avatar.close">
          </v-list-tile-avatar>

          <v-list-tile-content v-else>
            <img :src="avatar.open">
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-toolbar>

    <v-list class="pt-0" dense>
      <v-divider></v-divider>
      <v-list-tile v-for="item in items" :key="item.title" :class="{separator: item.separator}" >
        <a v-if="item.link" :href="item.link" target="_blank">
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>

          <v-list-tile-content>
            <v-list-tile-title>
              {{ item.title }}
            </v-list-tile-title>
          </v-list-tile-content>
        </a>

        <router-link v-if="item.route" :to="item.route">
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>

          <v-list-tile-content>
            <v-list-tile-title>
              {{ item.title }}
            </v-list-tile-title>
          </v-list-tile-content>
        </router-link>
      </v-list-tile>
    </v-list>
  </v-navigation-drawer>
</template>
<script src="./navigator-drawer.js"></script>
<style src="./navigator-drawer.scss" lang="scss"></style>
