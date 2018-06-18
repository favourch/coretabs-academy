<template>
<div class="inner-header">
  <v-toolbar app class="white">
    <v-toolbar-side-icon v-on:click="$parent.$emit('toggle-drawer')"></v-toolbar-side-icon>
    <v-toolbar-title class="mx-auto">{{title}}</v-toolbar-title>
    <v-avatar class="brand-logo">
        <router-link to="/">
          <img :src="$store.state.icon" alt="coretabs" />
        </router-link>
    </v-avatar>
  </v-toolbar>
</div>
</template>
<script src="./inner-header.js"></script>
<style src="./inner-header.scss" lang="scss"></style>
