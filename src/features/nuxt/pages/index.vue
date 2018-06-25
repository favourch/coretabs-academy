<template>
<div id="home">
  <v-container fluid fill-height>
    <v-layout fluid row justify-center wrap>
      <v-flex text-xs-center xs10 sm8 md5 id="introductory-video">
        <v-btn id="play" @click="play(vPlayer)"><i></i></v-btn>
          <div id="player" v-video-player:vPlayer="playerOptions" class="vjs-custom-skin" @pause="pause($event)" @ended="ended($event)">
          </div>
      </v-flex>
      <v-flex text-xs-right xs10 sm8 md5 id="introduction">
        <h2 class="black--text">{{i18n.heading_text}}</h2>
        <p class="black--text mt-4 mb-0">{{i18n.description_text_1}}></p>
        <p class="black--text mt-4 mb-0">{{i18n.description_text_2}}</p>
        <div id="introduction-buttons">
          <v-btn id="yes" round dark class="mt-4 mb-0 mr-0 ml-3">{{i18n.yes_btn_text}}</v-btn>
          <v-btn id="no" round light class="mt-4 mb-0 mx-0">{{i18n.no_btn_text}}</v-btn>
        </div>
      </v-flex>
    </v-layout>
  </v-container>
</div>
</template>
<script src="./index.js"></script>
<style src="./index.scss" lang="scss" scoped></style>
