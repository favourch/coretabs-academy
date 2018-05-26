<template>
    <v-container id="not-ready" fluid >
      <v-layout align-center justify-center>
        <v-flex id="container" class="text-xs-center" align-center xs12 sm10 lg7>
         <div id="statistics-padding">
            <h1 class="black--text mb-4 mt-5" v-html="i18n.heading_text[0]"></h1>
            <p class="black--text mb-5" v-html="i18n.description_text[0]"></p>
            <p class="black--text mb-5" id="source-text" v-html="i18n.source_text"></p>
            <v-layout v-for="(statistic, i) in i18n.statistics" :reverse="i%2 === 1" :key="i" row wrap align-center justify-center mb-5 pt-5>
              <v-flex :class="['statistics-img', 'img-'+ i]" sm12 md6>
              </v-flex>
              <v-flex :class="['statistics-desc','text-sm-center', i%2 === 1 ? 'text-md-left': 'text-md-right']" sm12 md6 >
                <span v-html="statistic.value"></span>
                <p v-html="statistic.desc"></p>
              </v-flex>
            </v-layout>
          </div>
          <v-layout >
            <div id="go-signup">
              <h1 class="black--text mb-4 mt-5" v-html="i18n.heading_text[1]"></h1>
              <p class="black--text mb-5" v-html="i18n.description_text[1]"></p>
              <v-btn id="yes-button" to="/signup" round dark v-html="i18n.yes_btn_text"></v-btn>
            </div>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-container>
</template>
<script src="./not-ready.js"></script>
<style src="./not-ready.scss" lang="scss"></style>
