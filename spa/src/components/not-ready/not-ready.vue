<template>
    <v-container id="not-ready" fluid >
      <v-layout align-center justify-center>
        <v-flex id="container" class="text-xs-center" align-center xs12 sm10 lg6>
         <div id="statistics-padding">
            <h1 class="black--text mb-4 mt-5" v-html="heading_text[0]"></h1>
            <p class="black--text mb-5" v-html="description_text[0]"></p>
            <p class="black--text mb-5" id="source-text" v-html="source_text"></p>
            <v-layout v-for="(statistic,index) in statistics" :reverse="statistic.reverse" :key="index" row wrap align-center justify-center mb-5 pt-5>
              <v-flex :class="['statistics-img','text-sm-center', statistic.reverse ? 'text-md-right': 'text-md-left']" sm12 md6 >
                <img src="~@/assets/multimedia/images/not-ready/self-taught.svg" alt="">
              </v-flex>
              <v-flex :class="['statistics-desc','text-sm-center', statistic.reverse ? 'text-md-left': 'text-md-right']" sm12 md6 >
                <span v-html="statistic.value"></span>
                <p v-html="statistic.desc"></p>
              </v-flex>
            </v-layout>
          </div>
          <v-layout >
            <div id="test">
              <h1 class="black--text mb-4 mt-5" v-html="heading_text[1]"></h1>
              <p class="black--text mb-5" v-html="description_text[1]"></p>
              <v-btn id="yes" round dark v-html="button_text"></v-btn>
            </div>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-container>
</template>
<script src="./not-ready.js"></script>
<style src="./not-ready.scss" lang="scss"></style>
