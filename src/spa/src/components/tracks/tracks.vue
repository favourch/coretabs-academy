<template>
  <v-container id="tracks" fluid grid-list-xl fill-height>
    <v-layout justify-center wrap align-center>
      <v-flex xs12 md12 lg10 xl8>
        <v-layout class="tracks-items" justify-center wrap>
          <v-flex xs10 md4>
            <v-card height="100%">
              <div class="pic-container">
                <img
                  :src="backendImg"
                  :alt="tracks.track.backend.heading"
                >
              </div>

              <div class="card__body">
                <v-card-title primary-title>
                  <div>
                    <h2 class="mb-0" v-html="tracks.track.backend.heading"></h2>
                  </div>
                </v-card-title>

                <v-card-text>
                    <p class="card__desc" v-html="tracks.track.backend.description"></p>
                </v-card-text>

                <v-card-actions>
                  <v-btn depressed round class="button" to="/not-ready"> {{tracks.track.discover_btn}} </v-btn>
                </v-card-actions>
              </div>
            </v-card>

          </v-flex>
          <v-flex xs10 md4>
            <v-card height="100%">
              <div class="pic-container">
                <img
                  :src="frontendImg"
                  :alt="tracks.track.frontend.heading"
                >
              </div>

              <div class="card__body">
                <v-card-title primary-title>
                  <div>
                    <h2 class="mb-0 " v-html="tracks.track.frontend.heading"></h2>
                  </div>
                </v-card-title>

                <v-card-text>
                    <p class="card__desc" v-html="tracks.track.frontend.description"></p>
                </v-card-text>

                <v-card-actions>
                  <v-btn depressed round class="button" to="/not-ready">{{tracks.track.discover_btn}}</v-btn>
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
<style src="./tracks.scss" lang="scss" scoped></style>
