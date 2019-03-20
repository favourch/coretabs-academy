<template>
<v-container id="certificate" fluid fill-height>
  <v-layout row align-center justify-center wrap>
     <!-- <img :src="output" width="1120" height="700"> -->
    <v-flex ref="download" id="certificate-container" xs11 md7>
      <v-layout row wrap>
        <v-flex xs12 md8>
          <div id="certificate-header">
            <img :src="$store.state.logo" alt="coretabs">
            <h2>Certificate of Complation</h2>
            <h3>Awarded to</h3>
          </div>

          <div id="certificate-name">
            <h1>{{ certificate.full_name }}</h1>
          </div>

          <div id="certificate-desc">
            <p>For complated the workshop</p>
            <h2>{{ certificate.heading }}</h2>
            <blockquote cite="http://coretabs.net">{{ firstName }} {{ certificate.body }}
            </blockquote>
          </div>

          <div id="certificate-footer">
            <div>{{ certificate.date }}</div>
            <p>www.coretabs.net/certificate/{{ certificateId }}</p>
          </div>

        </v-flex>
        <v-flex xs12 md4 id="certificate-signature">

          <div id="signature-img">
            <img :src="certificate.signature.url" alt="">
          </div>
            <div id="signature-name">
              {{ certificate.signature.name }}
            </div>
        </v-flex>
        <div id="certificate-ribbon"></div>
      </v-layout>
    </v-flex>
    <v-flex id="certificate-actions" sm12 md12>

      <v-layout class="mb-3" row align-center justify-center wrap>
        <v-flex xs12 md2 px-3>
          <v-btn class="mb-3" large :loading="loading" @click="download">
            <v-icon dark>save_alt</v-icon>تنزيل
          </v-btn>
        </v-flex>
        <v-flex xs12 md2 px-3>
          <v-btn dark color="green" large @click="shareCertificate">
            <v-icon dark>share</v-icon> مشاركة
          </v-btn>
        </v-flex>
      </v-layout>
      <v-dialog v-model="shareDialog" max-width="500">
        <v-card class="pa-2">
          <v-card-text v-if="!isCopied">
            <p>قم بنسخ الرابط التالي ومشاركتة مع زملائك</p>
            <div id="certificate-link-holder" @click="copyToClipboard">{{certificateLink}}</div>
            <input type="hidden" id="link-holder" :value="certificateLink">
          </v-card-text>
            <v-card-text class="text-xs-center" v-if="isCopied">
              <v-icon color="green" class="mb-3" large>check_circle</v-icon>
              <p class="subheading">تم نسخ الرابط بنجاح، بإمكانك الأن مشاركتة</p>
            </v-card-text>
            <v-card-text v-if="manualCopy">
              <p>قم بنسخ الرابط بشكل يدوي، ثم قم بمشاركته</p>
              <v-text-field :value="certificateLink"></v-text-field>
            </v-card-text>
        </v-card>
      </v-dialog>

    </v-flex>
  </v-layout>
</v-container>
</template>

<script src="./certificate.js"></script>

<style src="./certificate.scss" lang="scss" scoped></style>
