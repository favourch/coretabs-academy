<template>
<header v-show="show && $store.getters.header">
  <v-navigation-drawer :right="drawer.isRight" app temporary floating v-model="drawer.isOpen" :width="drawer.width">
    <v-list class="py-0">
      <template v-for="(nav, i) in navs">
        <v-list-tile  :key="i">
          <v-btn flat block large class="white--text menu-link" :to="nav.url" v-html="i18n[i]"></v-btn>
        </v-list-tile>
      </template>
    </v-list>
  </v-navigation-drawer>
  <v-toolbar :fixed="fixed" :flat="!fixed">
    <v-toolbar-items class="hidden-sm-and-down">
     <v-btn v-for="(nav, i) in navs" :key="i" flat :class="['white--text', nav.radius ? 'radius' : '']" :to="nav.url" v-html="i18n[i]"></v-btn>
    </v-toolbar-items>
    <v-toolbar-side-icon v-if="!drawer.isOpen" class="white--text drawer-icon hidden-md-and-up" @click="toggleDrawer()"></v-toolbar-side-icon>
    <v-toolbar-side-icon v-else class="white--text drawer-icon hidden-md-and-up" @click="toggleDrawer()">
      <v-icon>close</v-icon>
    </v-toolbar-side-icon>
    <v-spacer></v-spacer>
    <router-link to="/" class="brand-logo">
      <img :src="$store.state.logo" alt="coretabs" />
    </router-link>
  </v-toolbar>
</header>
</template>
<script src="./header.js"></script>
<style src="./header.scss" lang="scss"></style>
