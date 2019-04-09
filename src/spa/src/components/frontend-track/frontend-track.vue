<template>
<div id="track">

    <v-layout justify-center class="hero-container">
        <v-flex xs10 lg10 xl7>
            <v-card class="hero section section--dark card__edges" id="frontend-hero">

                <div class="hero__body">
                    <v-title class="section__header section__header--desc">
                        <h1 class="section__heading">مسار تطوير واجهات الويب</h1>
                        <h2 class="section__heading">(مستوى أول)</h2>
                        <p>في هذا المسار ستقوم بتطوير واجهات جميلة للمواقع الإلكترونية والتي من خلالها سيتفاعل المستخدمين مع التطبيق.</p>
                    </v-title>

                    <v-card-actions>
                        <v-btn depressed round class="button button--green" @click="scrollToPricing">انضم الآن</v-btn>
                    </v-card-actions>

                    <div class="hero__countdown">
                        <p class="hero__countdown-text">باب التقديم للدفعة القادمة يغلق خلال</p>

                        <Countdown deadline="April 18, 2019" labels="أيام-ساعة-دقيقة-ثانية"></Countdown>
                    </div>
                </div>

            </v-card>
        </v-flex>
    </v-layout>

    <section id="presentation">

        <v-layout justify-center wrap>
            <v-flex xs10 lg10 xl6 class="text-xs-center">
                <h1 class="mb-4">لماذا يجب عليك تعلم تطوير واجهات الويب</h1>
                <p>
                    مسار تطوير واجهات الويب - مستوى أول - يتكون من ثلاث مشاريع تطبيقية ستقوم ببنائها خلال فترة الدفعة التعليمية مع زملائك تحت توجيه المدربين والموجهين وفي بيئة تفاعلية. لا يتطلب منك في هذا المستوى أن يكون لديك أي خلفية برمجية.
                </p>
            </v-flex>
        </v-layout>

        <v-layout justify-center wrap>
            <v-flex xs10 lg10 xl6>

                <v-layout class="desc-box" wrap row>
                    <v-flex xs12 md5>
                        <div class="desc-image"></div>
                    </v-flex>
                    <v-flex class="desc-text desc-text__right" x12 md7>
                        <h2>ابدأ بمشاريع حقيقية </h2>
                        <p>مئات الكورسات في الإنترنت تدربك على البرمجة ولكن بمجرد أن تنتهي من الكورس <strong>ستتساءل</strong> إذا كنت قادراً على عمل مشروع فعلي؟
 أو إذا كنت مؤهلاً للحصول على وظيفة مبرمج.
                        </p>
                        <p>ولكن معنا ستتعلم البرمجة بشكل مختلف تماماً, حيث ستقوم ببناء <strong>مشاريع حقيقية</strong> في كل ورشة عمل.
                        </p>
                    </v-flex>
                </v-layout>

                <v-layout class="desc-box" wrap row reverse>
                    <v-flex xs12 md5>
                        <div class="desc-image"></div>
                    </v-flex>
                    <v-flex class="desc-text desc-text__left" x12 md7>
                        <h2>تدرب على أيدي مدربين خبراء</h2>
                        <p>نعلم تماماً أنك تريد التعلم على يد أفضل المدربين، لهذا سيقوم بتدريبك خبراء تم اختيارهم من ضمن <strong>أفضل عشرة</strong> مدربين في الشرق الأوسط من قبل مؤسسة دبي للمستقبل ولديهم خبرة تزيد على 8 سنوات في المجال.
                        </p>
                    </v-flex>
                </v-layout>

                <v-layout class="desc-box" wrap row reverse>
                    <v-flex xs12>
                        <blockquote class="quote">
                            نحن نؤمن دائماً أن الطريقة المثلى للتعلم, هي تطبيق ما تتعلمه بشكل مستمر.
                        </blockquote>
                    </v-flex>
                </v-layout>

                <v-layout class="desc-box" wrap row>
                    <v-flex xs12 md5>
                        <div class="desc-image"></div>
                    </v-flex>
                    <v-flex class="desc-text desc-text__right" x12 md7>
                        <h2>حقق أحلامك الريادية!</h2>
                        <p>نحن متأكدين أن لديك مشاريع ريادية وأفكار رائعة، في الحقيقة العديد من التطبيقات جعلت أصحابها من <strong>أثرياء العالم</strong>! من يدري قد يكون مشروعك هو المشروع الثوري التالي.
                        </p>
                        <p>معنا ستتعلم <strong>المهارات اللازمة</strong> لعمل تطبيقات ومشاريع ريادية ناجحة، لست بحاجة لأي معرفة سابقة أو شهادة جامعية، كل ماتحتاجه هو لابتوب وخط إنترنت.
                        </p>
                    </v-flex>
                </v-layout>

                <v-layout class="desc-box" wrap row reverse>
                    <v-flex xs12 md5>
                        <div class="desc-image"></div>
                    </v-flex>
                    <v-flex class="desc-text desc-text__left" x12 md7>
                        <h2>سنراجع معك مشاريعك التي تطبقها معنا</h2>
                        <p>ستواجهك العديد من المشاكل أثناء تعلم البرمجة لكن ليس هناك أسوأ من مواجهتها لوحدك, فربما تأخذ منك أسبوع لحل المشكلة, وربما تجد حلاً بطريقة خاطئة ولا أحد يوجهك للطريق الصحيح!
                        </p>
                        <p>لكن لا تقلق أبداً, سيكون لديك في مجتمع كورتابز العديد من المدربين والطلاب الذين سيساعدوك على تخطي هذه العقبات بسهولة بتوجيهك بشكل مستمر ومساعدتك على فهم التعقيدات.
                        </p>
                    </v-flex>
                </v-layout>

            </v-flex>

        </v-layout>
    </section>

    <v-layout justify-center class="gray-bg">
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
    </v-layout>

    <div id="work-preview" class="section section--light">

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
                <div class="avatar" :style="{ backgroundImage: 'linear-gradient(rgba(84, 0, 255, 0.4), rgba(202, 62, 75, 0.4)), url(' + testimonialsImages[i] + ')' }"></div>
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

            <div id="pricing" class="section section--light">
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
                                                <h2 class="mb-3 ">منحة تدريبية</h2>
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
            </div>

            <section id="other-tracks" class="section section--light text-xs-center text-md-right">
                <div class="section__header">
                    <h1 class="section__heading">مسارات أخرى</h1>
                </div>
                <v-layout justify-center>
                    <v-flex xs10 md6 id="other-tracks__card">
                        <v-layout justify-center align-center row wrap>
                          <v-flex xs12 md5 class="card__img">
                             <img src="https://source.unsplash.com/random/400x400" alt="مسار تطوير واجهات الويب">
                          </v-flex>
                          <v-flex xs12 md7 class="px-5 py-4">
                            <h2 class="mb-3">مسار تطوير واجهات الويب</h2>
                            <p class="card__desc">في هذا المسار ستقوم بتطوير واجهات جميلة للمواقع الإلكترونية والتي من خلالها سيتفاعل المستخدمين مع التطبيق.</p>
                            <v-btn depressed round class="button py-4 px-3 mt-4" to="/tracks">استكشف المسار</v-btn>
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
