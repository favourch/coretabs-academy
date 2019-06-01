<template>
  <v-scale-transition origin="bottom center 0">
    <div class="join-invite" v-if="!isClosed">

      <v-card>
        <v-card-title primary-title>
          <div>
            <h3 class="join-invite__title" v-html="i18n.heading"></h3>
            <p v-html="i18n.text"></p>
          </div>
        </v-card-title>

        <v-card-actions class="join-invite__actions">
          <v-btn class="join-invite__signup mt-4 mb-0 mr-0 ml-3" round dark to="/signup">{{ i18n.join_btn_text }}</v-btn>
          <v-btn class="join-invite__close mt-4 mb-0 mr-0 ml-3" round light @click="closeBanner">{{ i18n.close_btn_text}}</v-btn>
        </v-card-actions>

      </v-card>

    </div>
  </v-scale-transition>

</template>
<script src="./join-invite.js"></script>
<style src="./join-invite.scss" lang="scss"></style>
