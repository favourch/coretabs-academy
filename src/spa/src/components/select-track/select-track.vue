<template>
  <v-container id="select-track" fluid fill-height>
    <v-layout row align-center justify-center>
      <v-flex id="container" xs9 md6>
        <v-layout row align-center justify-center wrap>
          <v-flex class="track" xs12 sm6 md6>
            <div @click="select(track1)">
              <input type="radio" name="track" v-model="track_selected" :value="track1" />
              <v-icon class="custom-radio"></v-icon>
              <div class="logo"></div>
              <p v-html="i18n.track_1_text_en" class="mt-4 mb-2"></p>
              <p v-html="i18n.track_1_text_ar" class="mt-2 mb-4"></p>
            </div>
            <v-btn round class="submit" @click="submit" :disabled="track_selected != track1 || waiting">
              <v-progress-circular indeterminate size="24" class="ml-2" v-if="waiting"></v-progress-circular>
              {{ i18n.submit_btn_text }}
            </v-btn>
          </v-flex>
          <v-flex class="track" xs12 sm6 md6>
            <div @click="select(track2)">
              <input type="radio" name="track" v-model="track_selected" :value="track2" />
              <v-icon class="custom-radio"></v-icon>
              <div class="logo"></div>
              <p v-html="i18n.track_2_text_en" class="mt-4 mb-2"></p>
              <p v-html="i18n.track_2_text_ar" class="mt-2 mb-4"></p>
            </div>
            <v-btn round class="submit" @click="submit" :disabled="track_selected != track2 || waiting">
              {{ i18n.submit_btn_text }}
            </v-btn>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script src="./select-track.js"></script>
<style src="./select-track.scss" lang="scss"></style>
