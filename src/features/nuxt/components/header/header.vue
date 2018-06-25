<template>
<header v-show="show">
  <v-navigation-drawer :right="drawer.isRight" app temporary floating v-model="drawer.isOpen" :width="drawer.width">
    <v-list class="py-0">
      <template v-for="(nav, i) in navs">
            <v-list-tile v-if="!nav.dropdown" :key="i">
               <v-btn flat block large class="white--text" :to="nav.url" v-html="i18n[i]"></v-btn>
            </v-list-tile>
            <v-list-group v-else :key="i">
               <v-list-tile slot="activator">
                  <v-list-tile-content>
                     <v-list-tile-title v-html="i18n[i]"></v-list-tile-title>
                  </v-list-tile-content>
               </v-list-tile>
               <v-list-tile v-for="child in nav.children" :key="child.name">
                  <v-btn flat block large class="white--text" :to="child.url" v-html="child.name"></v-btn>
               </v-list-tile>
            </v-list-group>
         </template>
    </v-list>
  </v-navigation-drawer>
  <v-toolbar :fixed="fixed" :flat="!fixed">
    <v-toolbar-items class="hidden-sm-and-down">
      <v-btn v-for="(nav, i) in navs" :key="i" v-if="!nav.dropdown" flat :class="['white--text', nav.radius ? 'radius' : '']" :to="nav.url" v-html="i18n[i]"></v-btn>
      <v-menu v-else open-on-hover>
        <v-btn flat large class="white--text" slot="activator" v-html="i18n[i]"></v-btn>
        <v-list class="primary white--text nav-dropdown py-0">
          <v-list-tile v-for="child in nav.children" :key="child.name">
            <v-btn flat large class="white--text" v-html="child.name"></v-btn>
          </v-list-tile>
        </v-list>
      </v-menu>
    </v-toolbar-items>
    <v-toolbar-side-icon class="white--text hidden-md-and-up" @click="toggleDrawer()"></v-toolbar-side-icon>
    <v-spacer></v-spacer>
    <nuxt-link to="/" class="brand-logo">
      <img src="~assets/multimedia/icons/logo.png" alt="coretabs" />
    </nuxt-link>
  </v-toolbar>
</header>
</template>
<script src="./header.js"></script>
<style src="./header.scss" lang="scss" scoped></style>
