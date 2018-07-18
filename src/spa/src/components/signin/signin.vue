<template>
  <div id="signin">
    <v-container fluid fill-height>
      <v-layout row wrap align-center justify-center>
        <v-flex id="container" >
          <v-layout row justify-center>
            <v-flex xs12>
              <v-alert type="error" row xs12 class="mb-4" v-model="alert.error" v-text="alert.message"></v-alert>
            </v-flex>
          </v-layout>
          <v-layout row align-center justify-center>
            <v-flex id="splash" xs0 sm0 md6>
            </v-flex>
            <v-flex id="form" xs12 sm12 md6>
              <v-form ref="form" lazy-validation>
                <h2 class="black--text mb-2" v-html="i18n.heading_text"></h2>
                <v-text-field :label="form.email_label" v-model="email" :class="[alert.success ? 'disabled' : '']" :rules="emRules" :disabled="alert.success" dir="auto" @keyup.enter="submit" autocomplete="on" name="email" style="-webkit-autofill: none;" required></v-text-field>
                <v-text-field :label="form.password_label" v-model="password" :class="[alert.success ? 'disabled' : '']" :rules="pwRules" :disabled="alert.success" dir="auto" @keyup.enter="submit" required
                              :append-icon="pw ? 'visibility' : 'visibility_off'" :append-icon-cb="() => (pw = !pw)" :type="pw ? 'password' : 'text'" ></v-text-field>
                <p id="forgot" v-html="i18n.forgot_link_text" class="black--text mt-1 mb-1"></p>
                <div id="buttons">
                  <v-btn round id="submit" @click="submit" v-show="!alert.success" :disabled="!valid || waiting">
                    <v-progress-circular indeterminate size="24" class="ml-2" v-if="waiting"></v-progress-circular>
                    {{ i18n.submit_btn_text }}
                  </v-btn>
                  <router-link round id="signup" to="/signup" v-html="i18n.signup_btn_text"></router-link>
                </div>
              </v-form>
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>
<script src="./signin.js"></script>
<style src="./signin.scss" lang="scss"></style>
