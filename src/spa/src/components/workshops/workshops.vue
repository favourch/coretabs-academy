<template>
  <div v-if="loaded" class="workshops">
    <NavigatorDrawerComponent />
    <section id="row-flexed">
      <v-navigation-drawer id="sidenav" :right="drawer.isRight" v-model="drawer.isOpen" :width="$store.state.css.workshops.drawerWidth" hide-overlay>
        <v-toolbar flat>
          <v-toolbar-title v-html="i18n.title"></v-toolbar-title>
        </v-toolbar>
        <v-list class="py-0">
          <v-stepper v-model="current.workshop.index" vertical class="py-0">
            <v-list-group v-for="workshop in workshops" :key="`step-${workshop.index}`">
              <v-list-tile slot="activator">
                <v-stepper-step :step="workshop.index" :complete="workshop.shown_percentage === 100" :class="{'stepper__step--active':workshop.shown_percentage > 0}">
                  <router-link :to="workshop.url">{{workshop.title}}</router-link>
                </v-stepper-step>
              </v-list-tile>
            </v-list-group>
          </v-stepper>
        </v-list>
      </v-navigation-drawer>
      <section id="column-flexed">
        <inner-header-component :title="current.workshop.title"></inner-header-component>
        <div class="content" :style="{ height: height + 'px' }" v-resize="onResize">
          <router-view :workshop="current.workshop"></router-view>
        </div>
      </section>
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
<script src="./workshops.js"></script>
<style src="./workshops.scss" lang="scss"></style>
