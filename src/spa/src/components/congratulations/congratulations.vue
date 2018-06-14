<template>
  <v-container id="congratulations" fluid fill-height>
    <v-layout row align-center justify-center>
      <v-flex id="container" xs6>
        <v-layout row justify-center>
          <v-flex xs12>
            <v-alert type="success" row xs12 class="mb-4" v-model="alert.success" v-text="alert.message"></v-alert>
            <v-alert type="error" row xs12 class="mb-4" v-model="alert.error" v-text="alert.message"></v-alert>
          </v-flex>
        </v-layout>
        <v-layout row align-center justify-center>
          <v-flex id="splash" xs0 sm0 md6>
          </v-flex>
          <v-flex id="form" class="text-xs-right" xs12 sm12 md6>
            <v-form ref="form" lazy-validation>
              <h2 class="black--text mb-2" v-html="i18n.heading_title_text"></h2>
              <p v-html="i18n.description_text"></p>
              <v-btn round id="submit" @click="submit" v-html="counter > 0 ? counter : i18n.submit_btn_text  " :disabled="counter > 0"></v-btn>
            </v-form>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script src="./congratulations.js"></script>
<style src="./congratulations.scss" lang="scss"></style>
