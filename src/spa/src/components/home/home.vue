<template>
  <div id="home">
    <v-container fluid fill-height>
        <v-layout fluid row justify-center wrap>
          <v-flex text-xs-center xs10 sm8 md5 id="introductory-video" @click="play">
            <v-btn id="play"><i></i></v-btn>
          </v-flex>
          <v-flex text-xs-right xs10 sm8 md5 id="introduction">
              <h2 class="black--text" v-html="i18n.heading_text"></h2>
              <p class="black--text mt-4 mb-0" v-html="i18n.description_text_1"></p>
              <p class="black--text mt-4 mb-0" v-html="i18n.description_text_2"></p>
              <div id="introduction-buttons">
                <v-btn id="yes" round dark class="mt-4 mb-0 mr-0 ml-3" v-html="i18n.yes_btn_text"  to="/signup"></v-btn>
                <v-btn id="no" round light class="mt-4 mb-0 mx-0" v-html="i18n.explore_tracks_text" to="/tracks"></v-btn>
              </div>
          </v-flex>
        </v-layout>
    </v-container>
    <div class="video-modal" @click="closeModal">
      <div class="video-iframe">
        <youtube :video-id="videoId" ref="youtube" :player-vars="playerVars"></youtube>
      </div>
    </div>
  </div>
</template>
<script src="./home.js"></script>
<style src="./home.scss" lang="scss"></style>
