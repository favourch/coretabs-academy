<template>
  <v-container id="tracks" fluid grid-list-xl fill-height>
    <v-layout justify-center wrap align-center>
      <v-flex xs12 lg10>
        <v-layout class="tracks-items" justify-center wrap>
          <v-flex xs10 md4>
            <v-card height="100%">
              <div class="pic-container">
                <img
                  :src="backendImg"
                  alt="مسار تطوير النظم الخلفية"
                >
              </div>

              <div class="card__body">
                <v-card-title primary-title>
                  <div>
                    <h2 class="mb-0 ">مسار تطوير النظم الخلفية</h2>
                  </div>
                </v-card-title>

                <v-card-text>
                    <p class="card__desc">في هذا المسار ستقوم ببناء الأنظمة الخلفية للمواقع الإلكترونية وتصميم قواعد البيانات الخاصة بها.</p>
                </v-card-text>

                <v-card-actions>
                  <v-btn depressed round class="button" to="/not-ready">استكشف المسار</v-btn>
                </v-card-actions>
              </div>
            </v-card>

          </v-flex>
          <v-flex xs10 md4>
            <v-card height="100%">
              <div class="pic-container">
                <img
                  :src="frontendImg"
                  alt="مسار تطوير واجهات الويب"
                >
              </div>

              <div class="card__body">
                <v-card-title primary-title>
                  <div>
                    <h2 class="mb-0 ">مسار تطوير واجهات الويب</h2>
                  </div>
                </v-card-title>

                <v-card-text>
                    <p class="card__desc">في هذا المسار ستقوم بتطوير واجهات جميلة للمواقع الإلكترونية والتي من خلالها سيتفاعل المستخدمين مع التطبيق.</p>
                </v-card-text>

                <v-card-actions>
                  <v-btn depressed round class="button" to="/not-ready">استكشف المسار</v-btn>
                </v-card-actions>
              </div>
            </v-card>

          </v-flex>
         
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script src="./tracks.js"></script> 
<style src="./tracks.scss" lang="scss"></style> 
