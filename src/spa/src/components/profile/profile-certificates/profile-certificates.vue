<template>
  <div v-if="loaded && certificates && certificates.length > 0" class="certificates">
    <h2 class="certificates__title">الإنجازات</h2>

    <div class="card-grid">
      <v-card v-for="certificate in certificates" :key="certificate.index">
        <v-card-title class="">
          <h3 class="card-title">{{ certificate.heading }}</h3>
        </v-card-title>

        <v-divider></v-divider>

        <div class="card-meta">
          <div class="card-date-wrapper">
            <v-icon class="card-icon">event</v-icon>
            <div class="card-date">{{ certificate.date }}</div>
          </div>

          <v-spacer></v-spacer>
          <v-card-actions>
            <router-link :to="{name: 'certificate', params: {certificateId: certificate.id}}"  href="#" download="" class="download-btn">
              <v-icon class="card-icon">visibility</v-icon>
              معاينة
            </router-link>
          </v-card-actions>
        </div>
      </v-card>
    </div>
  </div>
  <div v-else-if="loaded && certificates && certificates.length === 0">
    <v-container fluid fill-height>
      <v-layout column align-center justify-center>
        <p>لا أمتلك أي شهادة الآن ولكنني أعمل على ذلك 💪</p>
      </v-layout>
    </v-container>
  </div>
  <div v-else class="progress-container contrast">
    <v-container fluid fill-height>
      <v-layout column align-center justify-center>
        <v-progress-circular indeterminate :size="$store.state.progress.size" :width="$store.state.progress.width" v-if="!$store.state.progress.error"></v-progress-circular>
        <div class="error text-center" v-else>!</div>
        <div class="text text-center">{{$store.state.progress.text}}</div>
      </v-layout>
    </v-container>
  </div>
</template>

<script src="./profile-certificates.js"></script>
<style src="./profile-certificates.scss" lang="scss"></style>
