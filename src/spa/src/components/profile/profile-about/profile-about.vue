<template>
  <div class="about mt-5 pa-0">
      <v-layout row wrap justify-space-between>
        <v-flex xs12 md6 class="mx-5">
          <div class="mb-5">
            <h2 class="mb-4 title">نبذة عني</h2>
            <p class="user-bio">
                هناك حقيقة مثبتة منذ زمن طويل وهي أن المحتوى المقروء لصفحة ما سيلهي القارئ عن التركيز على الشكل الخارجي للنص أو شكل توضع الفقرات في الصفحة التي يقرأها.
            </p>
          </div>

          <div class="mb-5">
            <h2 class="mb-4 title">اللغات التي أتحدث بها</h2>

            <div class="lang-items">
              <div class="lang-item" v-for="num in 3" :key="num">
                <div class="lang-img-wrapper">Ar</div>
                <span class="lang-title">العربية</span>
              </div>
            </div>
          </div>

          <!-- <div class="mb-5">
            <h2 class="mb-4 title">مهاراتي</h2>

            <v-chip small label outline v-for="n in 3" :key="n">Tag {{ n}}</v-chip>
          </div> -->
        </v-flex>

        <v-flex xs12 md3 class="mx-5 mb-5">
          <v-card>
            <div class="px-4">
              <div class="py-4">
                <v-card-title class="pa-0 pb-2">
                  <h4 class="mb-2 font-weight-bold">تاريخ الإنضمام</h4>
                </v-card-title>

                <v-card-text class="pa-0">
                  <div>1/1/2018</div>
                </v-card-text>
              </div>

              <v-divider></v-divider>

              <v-card-actions class="py-4">
                <a :class="`profile-icon ${icon.name}-icon`" :href="icon.url" target="_blank" v-for="(icon, i) in icons"
                  :key="i"></a>
              </v-card-actions>

            </div>
          </v-card>
        </v-flex>
      </v-layout>

  </div>
</template>

<script src="./profile-about.js"></script>
<style src="./profile-about.scss" lang="scss"></style>
