<template>
  <v-container id="forgot-password" fluid fill-height>
    <v-layout row align-center justify-center>
      <v-flex id="container">
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
            <v-form v-model="valid" ref="form" @submit.prevent lazy-validation>
              <h2 class="black--text mb-2" v-html="i18n.heading_text"></h2>
              <p v-html="i18n.forgot_text"></p>
              <v-text-field dir="auto" :label="form.email_label" v-model="email" :class="[alert.success ? 'disabled' : '']" :rules="emRules" :disabled="alert.success" @keyup.enter="submit" autocomplete="on" name="email" required></v-text-field>
              <v-btn round id="submit" @click="submit" v-show="!alert.success" :disabled="!valid || waiting">
                <v-progress-circular indeterminate size="24" class="ml-2" v-if="waiting"></v-progress-circular>
                {{ i18n.submit_btn_text }}
              </v-btn>
            </v-form>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script src="./forgot-password.js"></script>
<style src="./forgot-password.scss" lang="scss"></style>
