<template>
<div v-if="loaded" class="modules">
   <NavigatorDrawerComponent />
   <section id="row-flexed">
      <v-navigation-drawer id="sidenav" :right="drawer.isRight" v-model="drawer.isOpen" :width="$store.state.css.workshops.drawerWidth" hide-overlay>
         <v-toolbar flat>
            <v-btn flat icon color="white" :to="current.workshop.URL">
               <v-icon v-if="drawer.isRight">chevron_right</v-icon>
               <v-icon v-else>chevron_left</v-icon>
            </v-btn>
            <v-toolbar-title>{{current.workshop.title}}</v-toolbar-title>
         </v-toolbar>
         <modules-nav-component :modules="current.modules"></modules-nav-component>
      </v-navigation-drawer>
      <section id="column-flexed">
         <inner-header-component :title="current.lesson.title"></inner-header-component>
         <div class="content" v-bind:style="{ height: height + 'px' }" v-resize="onResize">
            <router-view></router-view>
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
<script src="./modules.js"></script>
<style src="./modules.scss" lang="scss"></style>
