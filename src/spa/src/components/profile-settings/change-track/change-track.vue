<template>
  <v-container id="change-track" fluid>
    <v-layout row wrap align-center justify-center>
      <v-flex>
        <v-form ref="form" lazy-validation>
          <v-alert type="success" v-model="alert.success" v-text="alert.message"></v-alert>
          <v-alert type="error" v-model="alert.error" v-text="alert.message"></v-alert>
          <p class="heading" v-text="i18n.heading_text"></p>
          <v-select :items="tracks" item-text="title" item-value="slug" v-model="track_selected" :label="i18n.select_text" content-class="change-track" single-line></v-select>
          <p class="sub-heading heading" v-text="i18n.hint_text"></p>
          <v-btn round flat @click="submit" :disabled="!track_selected || waiting">
            <v-progress-circular indeterminate size="24" class="ml-2" v-if="waiting"></v-progress-circular>
            {{ i18n.submit_btn_text }}
          </v-btn>
        </v-form>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script src="./change-track.js"></script>
<style src="./change-track.scss" lang="scss"></style>
