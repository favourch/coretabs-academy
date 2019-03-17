<template>
  <div class="about">
    <v-container class="mt-5 pa-0">
      <v-layout row wrap justify-space-between>
        <v-flex xs12 md6 class="mx-5">
          <div class="mb-5">
            <h2 class="mb-4 title">نبذة عني</h2>
            <p class="user-bio">
              لوريم ايبسوم دولار سيت أميت ,كونسيكتيتور أدايبا يسكينج أليايت,سيت دو أيوسمود تيمبو أنكايديديونتيوت لابوري ات دولار ماجنا أليكيوا . يوت انيم أد مينيمفينايم,كيواس نوستريدأكسير سيتاشن يللأمكو لابورأس نيسي يت أليكيوب أكس أيا كوممودو كونسيكيوات . ديواس
              أيوتي أريري دولار إن ريبريهينديرأيت فوليوبتاتي فيلايت أيسسي كايلليوم دولار أيو فيجايت
              نيولا باراياتيور. أيكسسيبتيور ساينت أوككايكات كيوبايداتات نون بروايدينت ,سيونت ان كيولبا
              كيو أوفيسيا ديسيريونتموليت انيم أيدي ايست لابوريوم
            </p>
          </div>

          <div class="mb-5">
            <h2 class="mb-4 title">اللغات التي أتحدث بها</h2>

            <div class="lang-items">
              <div class="lang-item" v-for="num in 3" :key="num">
                <div class="lang-img-wrapper">Ar</div>
                <span class="lang-title">اللغة العربية</span>
              </div>
            </div>
          </div>

          <div class="mb-5">
            <h2 class="mb-4 title">مهاراتي</h2>

            <v-chip small label outline v-for="n in 3" :key="n">Tag {{ n}}</v-chip>
          </div>
        </v-flex>

        <v-flex xs12 md3 class="mx-5 mb-5">
          <v-card>
            <div class="px-4">
              <div class="py-4">
                <v-card-title class="pa-0 pb-2">
                  <h4 class="caption font-weight-bold">تاريخ الإنضمام</h4>
                </v-card-title>

                <v-card-text class="pa-0">
                  <div>1/1/2018</div>
                </v-card-text>
              </div>

              <v-divider></v-divider>

              <v-card-actions class="py-4">
                <span
                  :class="`profile-icon ${icon}-icon`"
                  v-for="(icon, i) in icons"
                  :key="i"
                ></span>

              </v-card-actions>

            </div>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>

  </div>
</template>

<script src="./profile-about.js"></script>
<style src="./profile-about.scss" lang="scss"></style>
