 <template> 
 <div id="maintenance"> 
    <v-container fluid fill-height> 
      <v-layout row wrap align-center justify-center> 
        <v-flex id="container" > 
          <v-layout row align-center justify-center> 
            <v-flex id="splash" xs0 md6> 
            </v-flex> 
            <v-flex id="form" xs12 sm12 md6> 
              <h1 class="black--text mb-2" v-html="i18n.heading_text"></h1> 
              <p  v-html="i18n.desc"></p> 
            </v-flex> 
          </v-layout> 
        </v-flex> 
      </v-layout> 
  </v-container> 
  </div> 
</template> 
<script src="./maintenance.js"></script> 
<style src="./maintenance.scss" lang="scss"></style> 