<template>
  <v-container id="change-password" fluid>
    <v-layout row wrap align-center justify-center>
      <v-flex xs12 md8>
        <v-form ref="form" lazy-validation>
          <v-alert type="success" v-model="alert.success" v-text="alert.message"></v-alert>
          <v-alert type="error" v-model="alert.error" v-text="alert.message"></v-alert>
          <v-text-field :placeholder="i18n.old_password"  v-model="old_password" :rules="pwRules"
                        :append-icon="pw ? 'visibility' : 'visibility_off'" :append-icon-cb="() => (pw = !pw)" :type="pw ? 'password' : 'text'" :disabled="false" @keyup.enter="submit" required></v-text-field>
          <v-text-field :placeholder="i18n.new_password" v-model="new_password1" :rules="pwRules" type="password" @keyup.enter="submit" required></v-text-field>
          <v-text-field :placeholder="i18n.re_new_password" v-model="new_password2" :rules="pwRules" type="password" @keyup.enter="submit" required></v-text-field>
          <v-btn round flat v-text="i18n.submit_btn_text" @click="submit" :disabled="valid < 4"></v-btn>
        </v-form>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script src="./change-password.js"></script>
<style src="./change-password.scss" lang="scss"></style>
