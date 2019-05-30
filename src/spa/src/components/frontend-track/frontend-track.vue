<template>
  <div id="track">
    <v-layout justify-center class="hero-container">
      <v-flex xs12 lg10 xl7>
        <v-card class="hero section section--dark card__edges" id="frontend-hero">
          <div class="hero__body">
            <v-title class="section__header section__header--desc">
              <h1 class="section__heading">مسار تطوير واجهات الويب</h1>
              <p>في هذا المسار ستقوم بتطوير واجهات جميلة للمواقع الإلكترونية والتي من خلالها سيتفاعل المستخدمين مع التطبيق.</p>
            </v-title>

            <v-card-actions>
              <v-btn depressed round class="button button--green" @click="scrollToPricing">انضم الآن</v-btn>
            </v-card-actions>

            <div class="hero__countdown">
              <p class="hero__countdown-text">باب التقديم للدفعة القادمة يغلق خلال</p>

              <Countdown deadline="june 2, 2019" labels="أيام-ساعة-دقيقة-ثانية"></Countdown>
            </div>
          </div>
        </v-card>
      </v-flex>
      <div class="scroll-down">
        <a href="#why-this-track">
          <v-icon large>expand_more</v-icon>
        </a>
      </div>
    </v-layout>

    <section id="why-this-track">
      <v-layout justify-center wrap row>
        <v-flex xs12 class="text-xs-center px-3 mt-5">
          <h1 class="mb-4">لماذا يجب عليك تعلم تطوير واجهات الويب؟</h1>
          <p
            class="paragraph"
          >تطوير واجهات الويب من أبرز المهن المطلوبة في عصرنا فلا يوجد مشروع مرتبط بالإنترنت إلا ويلعب فية مطور الواجهات دور أساسي.</p>
        </v-flex>
        <v-flex xs12 md10 xl8 class="why-this-track__container">
          <v-layout justify-space-between wrap row class="text-xs-right mt-5">

            <v-flex xs12 md4 class="pa-4">
              <div class="why-this-track__card">
                <span><v-icon>business_center</v-icon></span>
                <h2 class="mb-4">الكثير من الوظائف</h2>
                <p>مع التطور السريع في تقنية المعلومات يزداد الطلب على المطورين بكثرة بنسبة نمو تعتبر الأسرع من معدل نمو جميع المهن الأخرى.</p>
              </div>
            </v-flex>

            <v-flex xs12 md4 class="pa-4">
              <div class="why-this-track__card">
                <span><v-icon>trending_up</v-icon></span>
                <h2 class="mb-4">متوسط دخل عالي</h2>
                <p>أغلب الشركات المتعلقة بالتقنية ذو دخل عالي، لهذا يعتبر معدل دخل مطوري الويب أعلى من معدل دخل جميع المهن الأخرى.</p>
              </div>
            </v-flex>

            <v-flex xs12 md4 class="pa-4">
              <div class="why-this-track__card">
                <span><v-icon>blur_on</v-icon></span>
                <h2 class="mb-4">مهنة الحاضر والمستقبل</h2>
                <p>في الوقت الذي يهدد فيه تطور التكنولوجيا باختفاء الكثير من الوظائف، تضل وظيفة المطور باقية فالبرمجة هي لغة المستقبل.</p>
              </div>
            </v-flex>
          </v-layout>
        </v-flex>
        <div class="scroll-down">
          <a href="#direct-path">
            <v-icon large>expand_more</v-icon>
          </a>
        </div>
      </v-layout>
    </section>

    <section id="direct-path">
      <v-layout justify-center wrap align-center fill-height>
        <v-flex xs10 lg10 xl6 class="text-xs-center maze-text">
          <h1 class="mb-4">لماذا تحتاج لأكاديمية كورتابز؟</h1>
          <p
            class="paragraph"
          >أقرب طريق من النقطة (أ) إلى النقطة (ب) هي خط مستقيم، معرفة ذلك الخط يتطلب سنوات من الخبرة لذا فنحن نعرف هذا الطريق جيداً وسنأخذ بيدك خطوة بخطوة من خلالة، فإذا كنت مستعداً لإختصار الوقت وتجنب المتاهه لتحقيق أهدافك فأنت في المكان الصحيح.</p>
        </v-flex>
        <video autoplay muted loop playsinline id="maze-video">
          <source src="../../assets/multimedia/images/track/maze.mp4" type="video/mp4">
        </video>
        <div class="scroll-down">
          <a href="#presentation">
            <v-icon large>expand_more</v-icon>
          </a>
        </div>
      </v-layout>
    </section>

    <section id="presentation" class="px-4">
      <v-layout justify-center wrap align-center>
        <v-flex xs12 lg10 xl6 class="text-xs-center presentation-heading">
          <h1 class="mb-4">ماهي المميزات التي ستحصل عليها؟</h1>
        </v-flex>
      </v-layout>

      <v-layout justify-center wrap column>
        <v-layout class="desc-box" wrap row>
          <v-flex x12 sm5>
            <div class="desc-image"></div>
          </v-flex>
          <v-flex class="desc-text desc-text__right" x12 sm7>
            <h2>العمل على مشاريع حقيقة</h2>
            <p>
              مئات الكورسات على الإنترنت تدربك على البرمجة ولكن بمجرد أن تنتهي من الكورس ستتساءل إذا كنت قادراً على عمل
              <strong>مشروع فعلي</strong>؟
            </p>
            <p>لكن معنا ستتعلم البرمجة بشكل مختلف تماماً، حيث ستقوم ببناء مشاريع حقيقية خلال ورش العمل.</p>
          </v-flex>
        </v-layout>

        <v-layout class="desc-box" wrap row reverse>
          <v-flex x12 sm5>
            <div class="desc-image"></div>
          </v-flex>
          <v-flex class="desc-text desc-text__left" x12 sm7>
            <h2>التدرّب على أيدي مدربين خبراء</h2>
            <p>
              نعلم تماماً أنك تريد التعلم على يد أفضل المدربين، لهذا سيقوم بتدريبك خبراء تم اختيارهم من ضمن
              <strong>أفضل عشرة</strong> مدربين في الشرق الأوسط من قبل مؤسسة دبي للمستقبل ولديهم خبرة تزيد على 8 سنوات في المجال.
            </p>
          </v-flex>
        </v-layout>

        <v-layout class="desc-box" wrap row reverse>
          <v-flex xs12>
            <blockquote
              class="quote"
            >نحن نؤمن أن الطريقة المثلى للتعلم، هي تطبيق ما تتعلمه بشكل مستمر.</blockquote>
          </v-flex>
        </v-layout>

        <v-layout class="desc-box" wrap row>
          <v-flex x12 sm5>
            <div class="desc-image"></div>
          </v-flex>
          <v-flex class="desc-text desc-text__right" x12 sm7>
            <h2>الحصول على إرشاد شخصي</h2>
            <p>
              أثناء رحلتك التدريبية على كورتابز ستحصل على توجية شخصي من قبل مدربينا حيث سيتم
              <strong>مراجعة مشاريعك</strong> ومساعدتك على تجاوز المشاكل والعقبات حال ما إن واجهتها.
            </p>
          </v-flex>
        </v-layout>

        <v-layout class="desc-box" wrap row reverse>
          <v-flex xs12 sm5>
            <div class="desc-image"></div>
          </v-flex>
          <v-flex class="desc-text desc-text__left" x12 sm7>
            <h2>تحقيق أحلامك الريادية</h2>
            <p>
              نحن متأكدين أن لديك مشاريع ريادية وأفكار رائعة، في الحقيقة العديد من التطبيقات جعلت أصحابها من
              <strong>أثرياء العالم</strong>! من يدري قد يكون مشروعك هو المشروع الثوري التالي.
            </p>
            <p>
              معنا ستتعلم
              <strong>المهارات التقنية اللازمة</strong> لإخراج مشروعك للحياة، لست بحاجة لأي معرفة سابقة كل ماتحتاجه هو لابتوب وخط إنترنت.
            </p>
          </v-flex>
        </v-layout>
      </v-layout>
    </section>

    <div id="testimonials">
      <div class="skew-box">
        <div class="particles"></div>
        <h1 v-html="i18n.testimonials.title"></h1>
        <p v-html="i18n.testimonials.description"></p>
      </div>
      <div class="testimonials-carousel">
        <div
          class="testimonials-carousel-item"
          v-for="(testimonial, i) in i18n.testimonials.carousel"
          :key="i"
          @mouseenter="stopTSiema()"
          @mouseleave="playTSiema()"
        >
          <img class="quotation" :src="quotationIcon">
          <div
            class="avatar"
            :style="{ backgroundImage: 'linear-gradient(rgba(84, 0, 255, 0.4), rgba(202, 62, 75, 0.4)), url(' + testimonialsImages[i] + ')' }"
          ></div>
          <div class="testimonial">
            <h3 class="name">
              {{ testimonial.name }}
              <span class="description">- {{ testimonial.description }}</span>
            </h3>
            <p class="quote" v-html="testimonial.quote"></p>
            <div class="rating">
              <img v-for="i in 5" :key="i" :src="calc(i, testimonial.rating)">
            </div>
            <div class="navigation">
              <img class="left" :src="navigation.left" @click="testimonialsSiema.next(1)">
              <img class="right" :src="navigation.right" @click="testimonialsSiema.prev(1)">
            </div>
          </div>
        </div>
      </div>
      <div class="controls t" ref="controlsT">
        <button
          v-for="(button, i) in i18n.testimonials.carousel.length"
          type="button"
          name="button"
          @click="showTestimonials(button - 1, $event)"
          :key="i"
        ></button>
      </div>

      <div class="scroll-down">
        <a href="#path-curriculum">
          <v-icon large>expand_more</v-icon>
        </a>
      </div>
    </div>

    <section id="path-curriculum">
      <v-layout justify-center wrap align-center>
        <v-flex xs10 lg10 xl6 class="text-xs-center mt-5">
          <h1 class="mb-4">ما الذي ستنجزة خلال المسار؟</h1>
          <p
            class="paragraph"
          >خلال هذا المسار ستقوم بالعمل على مشاريع رائعة لإضافتها لمعرض أعمالك والتي ستعكس مدى الخبرة التي إكتسبتها خلال رحلتك التدريبية.</p>
        </v-flex>
        <div class="scroll-down">
          <a href="#pricing">
            <v-icon large>expand_more</v-icon>
          </a>
        </div>
      </v-layout>
    </section>

    <!-- <v-layout justify-center class="gray-bg">
        <v-flex xs10 md6>
          <div id="tracks-content" class="section section--light">
            <div class="section__header">
              <h1 class="section__heading">المحتوى التدريبي</h1>
            </div>

            <v-expansion-panel>
              <v-expansion-panel-content v-for="(item, i) in 5" :key="i">
                <div slot="header" class="header">
                  <h2 class="header__title">أساسيات تطوير الويب</h2>

                  <p class="ma-0 header__desc">وصف للورشة</p>
                </div>

                <v-list class="pa-0">
                  <template v-for="(item, index) in 5">

                    <v-list-tile :key="index" avatar>

                      <v-list-tile-avatar>
                        <v-icon small>play_arrow</v-icon>
                      </v-list-tile-avatar>

                      <v-list-tile-content>
                        <h3>مقدمة عن تطوير واجهات الويب</h3>
                      </v-list-tile-content>

                    </v-list-tile>
                  </template>
                </v-list>
              </v-expansion-panel-content>
            </v-expansion-panel>
          </div>
        </v-flex>
    </v-layout>-->

    <!-- <div id="work-preview" class="section section--light">

        <div class="section__header section__header--desc">
          <h1 class="section__heading">ما الذي ستقوم ببنائه خلال هذا المستوى</h1>
          <p>مشاريع رائعة لعرض أعمالك تعكس الخبرات التي اكتسبتها خلال رحلتك التدريبية</p>
        </div>

        <v-container fluid grid-list-xl>
          <v-layout justify-center wrap align-center>
            <v-flex xs12>
              <v-layout class="track-works" justify-center wrap>
                <v-flex xs10 sm5 md3>
                  <v-card height="100%" class="card__edges">
                    <div class="pic-container">
                      <img
                      src="https://source.unsplash.com/random/400x400"
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
                      </div>
                  </v-card>

                </v-flex>

                <v-flex xs10 sm5 md3>
                  <v-card height="100%" class="card__edges">
                    <div class="pic-container">
                      <img
                      src="https://source.unsplash.com/random/400x400"
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

                      </div>
                  </v-card>

                </v-flex>

                <v-flex xs10 sm5 md3>
                  <v-card height="100%" class="card__edges">
                    <div class="pic-container">
                      <img
                      src="https://source.unsplash.com/random/400x400"
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

                      </div>
                  </v-card>
                </v-flex>
              </v-layout>
            </v-flex>
          </v-layout>
        </v-container>
    </div>-->

    <section>
      <v-layout id="pricing" justify-center wrap row fill-height align-center>
        <v-flex xs12 md8 xl6 class="px-3">
          <h1 class="text-xs-center">ابدأ ببناء حاضرك ومستقبلك المهني</h1>
          <v-layout justify-center wrap row align-center class="pricing-card">
            <v-flex xs12 md8 class="pricing-card__right pa-5 text-xs-center">
              <h2 class="mb-3">منحة تدريبية</h2>
              <p class="card__desc">احصل على منحة تدريبية مغطاة التكاليف</p>
              <span class="current-price my-4">$0</span>
              <v-btn depressed round class="button pa-4" to="/signup">قم بالتقديم الآن</v-btn>
            </v-flex>
            <v-flex xs12 md4 class="pricing-card__left pa-5">
              <h2 class="mb-3">شاملة</h2>
              <ul>
                <li>
                  <v-icon>check</v-icon>مشاريع تطبيقية
                </li>
                <li>
                  <v-icon>check</v-icon>توجية شخصي
                </li>
                <li>
                  <v-icon>check</v-icon>مجتمع من المطورين
                </li>
                <li>
                  <v-icon>check</v-icon>وصول لجميع المسارات
                </li>
              </ul>
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>
    </section>

    <!-- <div id="pricing" class="section section--light">
      <div class="section__header section__header--desc">
        <h1 class="section__heading">ابدأ ببناء حاضرك ومستقبلك المهني</h1>
        <p>مشاريع رائعة لمعرض أعمالك تعكس الخبرات التي اكتسبتها خلال رحلتك التدريبية</p>
      </div>

      <v-layout justify-center wrap align-center>
        <v-flex xs12>
          <v-layout justify-center>
            <v-flex xs10 sm6 md3>
              <v-card class="card__edges">
                <div id="right-icon">
                  <v-icon>done</v-icon>
                </div>

                <div class="card__body">
                  <v-card-title primary-title>
                    <div class="card__header">
                      <h2 class="mb-3">منحة تدريبية</h2>
                      <p class="card__desc">احصل على منحة تدريبية مغطاة التكاليف</p>
                    </div>
                  </v-card-title>

                  <v-card-text>
                    <span class="price price--prev">$149</span>
                    <p class="price price--current">$0</p>
                  </v-card-text>

                  <v-card-actions>
                    <v-btn depressed round class="button pa-4" to="/signup">قم بالتقديم الآن</v-btn>
                  </v-card-actions>
                </div>
              </v-card>
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>
    </div>-->

    <section id="other-tracks" class="section section--light">
      <v-layout justify-center wrap row align-center>
        <v-flex xs12 class="text-xs-center">
          <h1 class="mb-4">مسارات أخرى</h1>
        </v-flex>
        <v-flex xs12 class="text-xs-center pa-3">
          <v-layout justify-center wrap row align-center>
            <v-flex xs12 md9 xl6 class="text-xs-center">
              <v-layout wrap row class="track-card">
                <v-flex xs12 md5 class="track-card__img">
                  <img
                    src="../../assets/multimedia/images/tracks/backend.png"
                    alt="مسار تطوير واجهات الويب"
                  >
                </v-flex>
                <v-flex xs12 md7 class="pa-5">
                  <h2 class="mb-3">مسار تطوير النظم الخلفية</h2>
                  <p
                    class="card__desc"
                  >في هذا المسار ستقوم ببناء الأنظمة الخلفية للمواقع الإلكترونية وتصميم قواعد البيانات.</p>
                  <v-btn depressed round class="button py-4 px-3 mt-4" to="/tracks/frontend">استكشف المسار</v-btn>
                </v-flex>
              </v-layout>
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>
    </section>

    <footer>
      <router-link to="/contact-us" v-html="i18n.footer.contactUs"></router-link>|
      <router-link to="/page/terms-of-service" v-html="i18n.footer.termsOfService"></router-link>|
      <router-link to="/page/privacy-policy" v-html="i18n.footer.privacyPolicy"></router-link>
    </footer>
  </div>
</template>

<script src="./frontend-track.js"></script>

<style src="./frontend-track.scss" lang="scss" ></style>
