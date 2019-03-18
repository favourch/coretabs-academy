<template>
  <v-container id="application-submitted" fluid fill-height>
    <v-layout row align-center justify-center>
      <v-flex id="container">
        <v-layout row align-center justify-center>
          <v-flex id="splash" xs0 sm0 md6>
          </v-flex>
          <v-flex id="form" class="text-xs-right" xs12 sm12 md6>
            <v-form ref="form" lazy-validation>
              <h2 class="black--text mb-4" v-html="i18n.heading_title_text"></h2>
              <p v-html="i18n.description_text"></p>
              <v-btn round id="back-home" v-html="i18n.start_btn_text" href="https://forums.coretabs.net/login"></v-btn>
            </v-form>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script src="./application-submitted.js"></script>
<style src="./application-submitted.scss" lang="scss"></style>
