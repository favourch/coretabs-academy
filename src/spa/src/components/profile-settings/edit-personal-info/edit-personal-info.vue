<template>
  <div :dir="$store.state.rev_direction">
    <v-container fluid>
      <v-layout row wrap>
        <v-flex d-flex class="mother-container">
          <v-layout row wrap>
            <v-flex xs12 md4 class="grid-container">
              <v-layout row wrap>
                <v-flex xs12 sm4 md12 class="image-container">
                  <div class="pic-border">
                     <label for="file_uploader" class="cursor-pointer">
                        <img class="pic" :src="avatar_url" />
                     </label>
                    <label for="file_uploader" class="leave cursor-pointer">
                      <v-icon small>edit</v-icon>
                      <input @change="previewImage($event)" v-show="false" name="avatar" type="file" id="file_uploader" accept="image/*"/>
                    </label>
                  </div>
                </v-flex>
                <v-flex xs12 sm8 md12 d-flex justify-center align-center class="info-container no-select text-center">
                  <div class="">
                    <h3 v-html="fullname"></h3>
                    <span v-html="`@${username}`"></span>
                  </div>
                  </v-flex>
                </v-layout>
            </v-flex>
            <v-flex xs12 md8 d-flex>
              <div class="form-container">
                <v-form ref="form" lazy-validation>
                  <v-alert type="success" v-model="alert.success" v-text="alert.message"></v-alert>
                  <v-alert type="error" v-model="alert.error" v-text="alert.message"></v-alert>
                  <v-text-field dir="auto" :label="form.fullname_label" v-model="fullname" :rules="fnRules" @keyup.enter="submit" required></v-text-field>
                  <v-text-field dir="auto" :label="form.email_label" v-model="email" :rules="emRules" @keyup.enter="submit" required></v-text-field>
                  <v-text-field dir="auto" :label="form.username_label" v-model="username" :rules="unRules" @keyup.enter="submit" required></v-text-field>
                  <v-btn right round id="submit" v-html="i18n.submit_btn_text" @click="submit" :disabled="valid < 4"></v-btn>
                </v-form>
              </div>
            </v-flex>
          </v-layout>

        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>
<script src="./edit-personal-info.js"></script>
<style src="./edit-personal-info.scss" lang="scss"></style>
