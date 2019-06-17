<template>
<div :dir="$store.state.rev_direction">
  <v-container fluid>
    <v-layout row wrap>
      <v-flex d-flex class="mother-container">
        <v-layout row wrap>
          <v-flex xs12 d-flex>
            <div class="form-container">
              <v-form ref="form" lazy-validation>
                <v-alert type="success" v-model="alert.success" v-text="alert.message"></v-alert>
                <v-alert type="error" v-model="alert.error" v-text="alert.message"></v-alert>
                <v-text-field dir="auto" :label="form.description" v-model="description" @keyup.enter="submit" required></v-text-field>
                <v-text-field dir="auto" :label="form.bio" v-model="bio" @keyup.enter="submit" required></v-text-field>
                <v-autocomplete :options="countries" option-value="value" option-text="text" :input-value="userCountry" :rules="crRules" v-model="userCountry" />
                <v-select v-model="userSkills" :items="skills" attach chips :label="form.skills" multiple></v-select>
                <v-text-field dir="auto" prepend-icon="fab fa-github" :label="form.github_link" v-model="github_link" @keyup.enter="submit"></v-text-field>
                <v-text-field dir="auto" prepend-icon="fab fa-linkedin" :label="form.linkedin_link" v-model="linkedin_link" @keyup.enter="submit"></v-text-field>
                <v-text-field dir="auto" prepend-icon="fab fa-facebook-square" :label="form.facebook_link" v-model="facebook_link" @keyup.enter="submit"></v-text-field>
                <v-text-field dir="auto" prepend-icon="fab fa-twitter" :label="form.twitter_link" v-model="twitter_link" @keyup.enter="submit"></v-text-field>
                <v-text-field dir="auto" prepend-icon="fas fa-globe" :label="form.website_link" v-model="website_link" @keyup.enter="submit"></v-text-field>
                <v-btn right round id="submit" @click="submit" :disabled="!valid || waiting">
                  <v-progress-circular indeterminate size="24" class="ml-2" v-if="waiting"></v-progress-circular>
                  {{ i18n.submit_btn_text }}
                </v-btn>
              </v-form>
            </div>
          </v-flex>
        </v-layout>

      </v-flex>
    </v-layout>
  </v-container>
</div>
</template>

<script src="./edit-profile-info.js"></script>

<style src="./edit-profile-info.scss" lang="scss"></style>
