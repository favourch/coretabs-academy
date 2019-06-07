<template>
  <div id="about">
    <div id="presentation">
      <div v-for="(section, i) in i18n.sections" :key="i" id="desc-box">
        <div class="description">
          <div class="desc-text">
            <h1 v-html="section.header"></h1>
            <p v-html="section.paragraph"></p>
          </div>
        </div>
        <div class="desc-image">
          <img :src="sectionsImages[i]" :alt="section.alt">
        </div>
      </div>
    </div>
    <div id="testimonials">
      <div class="skew-box">
        <div class="particles"></div>
        <h1 v-html="i18n.testimonials.title"></h1>
        <p v-html="i18n.testimonials.description"></p>
      </div>
      <div class="testimonials-carousel">
        <div class="testimonials-carousel-item" v-for="(testimonial, i) in i18n.testimonials.carousel" :key="i" @mouseenter="stopTSiema()" @mouseleave="playTSiema()">
          <img class="quotation" :src="quotationIcon" />
          <div class="avatar" :style="{ backgroundImage: 'linear-gradient(rgba(84, 0, 255, 0.4), rgba(202, 62, 75, 0.4)), url(' + testimonialsImages[i] + ')' }" />
          <div class="testimonial">
            <h3 class="name">
              {{ testimonial.name }}
              <span class="description"> - {{ testimonial.description }}</span>
            </h3>
            <p class="quote" v-html="testimonial.quote"></p>
            <div class="rating">
              <img v-for="i in 5" :key="i" :src="calc(i, testimonial.rating)" />
            </div>
            <div class="navigation">
              <img class="left" :src="navigation.left" @click="testimonialsSiema.next(1)">
              <img class="right" :src="navigation.right" @click="testimonialsSiema.prev(1)">
            </div>
          </div>
        </div>
      </div>
      <div class="controls t" ref="controlsT">
        <button v-for="(button, i) in i18n.testimonials.carousel.length" type="button" name="button" @click="showTestimonials(button - 1, $event)" :key="i"></button>
      </div>
    </div>

    <div id="team">
      <h1 v-html="i18n.team.title"></h1>
      <p v-html="i18n.team.description"></p>
      <div class="flex">
        <div class="box" v-for="(member, i) in i18n.team.members" :key="i">
          <div class="image-container">
            <img :src="teamImages[i]">
          </div>
          <div class="filter"></div>
          <div class="profile">
            <div class="profile-container">
              <h3 v-html="member.name"></h3>
              <p class="paragraph" v-html="member.about"></p>
              <div class="social">
                <div class="icon" v-for="(link, i) in member.links" v-if="link.src" :key="i">
                  <a :href="link.src" :title="link.name" target="_blank"></a>
                  <img :src="icons[link.name]" :alt="link.name">
                </div>
              </div>
            </div>
          </div>
       </div>
      </div>
    </div>

    <div id="contributors">
      <h1 v-html="i18n.contributors.title"></h1>
      <p v-html="i18n.contributors.description"></p>
      <div class="flex">
        <div class="box" v-for="(member, i) in i18n.contributors.members" :key="i">
          <div class="image-container">
            <img :src="contributorsImages[i]">
          </div>
          <div class="filter"></div>
          <div class="profile">
            <div class="profile-container">
              <h3 v-html="member.name"></h3>
              <p class="paragraph" v-html="member.about"></p>
              <div class="social">
                <div class="icon" v-for="(link, i) in member.links" v-if="link.src" :key="i">
                  <a :href="link.src" :title="link.name" target="_blank"></a>
                  <img :src="icons[link.name]" :alt="link.name">
                </div>
              </div>
            </div>
          </div>
       </div>
      </div>
    </div>

    <div id="mentors">
      <h1 v-html="i18n.mentors.title"></h1>
      <p v-html="i18n.mentors.description"></p>
      <div class="mentors-carousel">
        <div class="mentors-carousel-item" v-for="(member, i) in i18n.mentors.members" :key="i" :ref="'item' + i" @mouseenter="stopMSiema()" @mouseleave="playMSiema()">
          <div class="image-container">
            <img :src="mentorsImages[i]" :ref="'img'+i" class="photo">
          </div>
          <div class="filter"></div>
          <div class="profile">
            <div class="profile-container">
              <h3 v-html="member.name"></h3>
              <p class="paragraph" v-html="member.about"></p>
              <div class="social">
                <div class="icon" v-for="(link, i) in member.links" v-if="link.src" :key="i">
                  <a :href="link.src" :title="link.name" target="_blank"><img :src="icons[link.name]" :alt="link.name"></a>
                </div>
              </div>
            </div>
          </div>
       </div>
      </div>
      <div class="navigation">
        <img class="left" :src="navigation.left" @click="prev()" @mouseenter="stopMSiema()" @mouseleave="playMSiema()">
        <img class="right" :src="navigation.right" @click="next()" @mouseenter="stopMSiema()" @mouseleave="playMSiema()">
      </div>
      <div class="controls m" ref="controlsM" style="direction: ltr">
        <button v-for="(button, i) in mentorsSliderCount()" type="button" name="button" @click="showMentors(button - 1, $event)" :key="i"></button>
      </div>
    </div>

    <footer>
      <router-link to="/contact-us" v-html="i18n.footer.contactUs"></router-link>|
      <router-link to="/page/terms-of-service" v-html="i18n.footer.termsOfService"></router-link>|
      <router-link to="/page/privacy-policy" v-html="i18n.footer.privacyPolicy"></router-link>
    </footer>
  </div>
</template>
<script src="./about.js"></script>
<style src="./about.scss" lang="scss"></style>
