<template>
  <div v-if="loaded" class="lesson">
    <template v-if="['0', '1'].includes($parent.current.lesson.type)">
      <div :id="($parent.current.lesson.type === '0') ? 'lesson-youtube' : 'lesson-scrimba'"
        :class="['lesson-video', ($parent.current.lesson.type === '0') ? 'lesson-youtube' : 'lesson-scrimba']">
        <iframe v-if="$parent.current.lesson.type === '0'" :src="content.video+'?showinfo=0&rel=0'" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
        <iframe v-else :src="content.video"></iframe>
        <v-tabs :id="($parent.current.lesson.type === '0') ? 'youtube-tabs' : 'scrimba-tabs'" :right="$store.state.direction === 'rtl'" icons-and-text v-model="content.tab">
          <v-tab v-for="(tab, i) in i18n.video.tabs" :key="i">
            {{tab.text}}
            <v-icon>{{tab.icon}}</v-icon>
          </v-tab>
          <div v-if="$parent.current.lesson.type === '1'" id="scrimba-logo">
            <span>Workspace by</span>
            <a :href="content.video" title="open in new window" target="_blank"><img src="../../assets/multimedia/images/scrimba-logo.png" width="88" height="19" alt="scrimba"></a>
          </div>
        </v-tabs>
        <v-tabs-items v-model="content.tab">
          <v-tab-item id="0" key="0">
            <div class="lesson-markdown" v-html="content.markdown"></div>
          </v-tab-item>
          <v-tab-item id="1" key="1">
            <v-container id="have-question no-select" fluid grid-list-xl>
              <v-layout row wrap align-center justify-center>
                <v-flex sm12>
                  <v-layout class="tab-question" row align-center>
                    <img id="forum-logo" :src="$store.state.forumLogo" alt="forum-logo icon">
                    <div class="text">
                      <h4 v-html="i18n.video.question.title"></h4>
                      <div>{{ i18n.video.question.text }} <a :href="$parent.current.workshop.forums" target="_blank">{{ i18n.video.question.here }}</a></div>
                    </div>
                  </v-layout>
                </v-flex>
              </v-layout>
            </v-container>
          </v-tab-item>
        </v-tabs-items>
      </div>
    </template>
    <template v-if="$parent.current.lesson.type === '2'">
      <div class="lesson-markdown" v-html="content.markdown"></div>
    </template>
    <template v-if="$parent.current.lesson.type === '3'">
      <v-container id="lesson-quiz" class="lesson-quiz" fluid>
        <v-layout row wrap align-center justify-center class="quizz-layout">
          <v-flex xs10 md6>
            <v-stepper v-model="quiz.currentQuestion" class="quizz-stepper" non-linear>
              <v-stepper-header>
                <template v-for="(question, qIndex) in quiz.questions">
                  <v-stepper-step :class="question.hasOwnProperty('success') ? (question.success) ? 'true_step' : 'wrong_step' : null" :step="qIndex+1" :key="qIndex" :complete="quiz.currentQuestion > qIndex+1"></v-stepper-step>
                  <v-divider v-if="qIndex + 1 < quiz.questions.length" :key="`divider-${qIndex}`"></v-divider>
                </template>
              </v-stepper-header>
              <v-stepper-items>
                <v-card v-show="quiz.currentQuestion <= quiz.questions.length" flat>
                  <p class="question-num py-0">{{ i18n.quiz.steppers.question }} {{quiz.currentQuestion}} {{ i18n.quiz.steppers.from }} {{quiz.questions.length}} : {{i18n.quiz.heading_text}}</p>
                </v-card>
                <template v-for="(question, qIndex) in quiz.questions">
                  <v-stepper-content :step="qIndex + 1" :key="qIndex" :class="{checkboxes : (question.correct.length > 1) }">
                    <h3 class="question-content">{{question.text}}</h3>
                    <v-card color="grey lighten-1" flat>
                      <v-list three-line subheader>
                        <template v-for="(answer, aIndex) in question.answers">
                          <v-list-tile @click="chooseAnswer(question, aIndex)" :key="aIndex" :class="[question.choose.includes(aIndex) && !question.correct.includes(aIndex) && question.correct.length === 1 ? 'wrong_answer' : '' ,question.choose.includes(aIndex) && question.correct.includes(aIndex) && question.correct.length === 1 ? 'true_answer' : '',question.correct.includes(aIndex) && question.correct.length > 1 ? question.status : '']" >
                            <v-list-tile-action>
                              <input type="checkbox" v-model="question.choose" :value="answer" />
                              <span class="checkbox_cont">
                                <v-icon color="white" v-show="question.choose.includes(aIndex)" class="checkbox_inner" small></v-icon>
                              </span>
                            </v-list-tile-action>
                            <v-list-tile-content>
                              <v-list-tile-title>{{answer}}</v-list-tile-title>
                            </v-list-tile-content>
                          </v-list-tile>
                        </template>
                      </v-list>
                    </v-card>
                    <v-card v-show="question.result === i18n.quiz.results_texts.fail" flat>
                      <p class="hint-container py-0"><span class="circle"><v-icon color="white" small>lightbulb_outline</v-icon></span> {{question.hint}}</p>
                    </v-card>
                  </v-stepper-content>
                </template>
                <v-card class="btns-control" flat>
                  <v-btn v-show="quiz.currentQuestion < quiz.questions.length" class="r-btn" flat @click="quiz.currentQuestion++" :disabled="!quiz.questions[quiz.currentQuestion - 1].result">{{i18n.quiz.buttons_texts.next}}</v-btn>
                  <v-btn v-if="quiz.currentQuestion > 0" v-show="quiz.questions[quiz.currentQuestion - 1].correct.length > 1" class="r-btn" flat @click="checkAnswers(quiz.questions[quiz.currentQuestion - 1])">{{i18n.quiz.buttons_texts.confirm}}</v-btn>
                  <v-btn v-show="quiz.currentQuestion > 1" class="r-btn" flat @click="quiz.currentQuestion--">{{i18n.quiz.buttons_texts.pre}}</v-btn>
                  <span class="result-container">
                    <span :class="['result', quiz.questions[quiz.currentQuestion - 1].result === i18n.quiz.results_texts.fail ? 'err' : '']">{{quiz.questions[quiz.currentQuestion - 1].result}}</span>
                  </span>
                </v-card>
              </v-stepper-items>
            </v-stepper>
          </v-flex>
        </v-layout>
      </v-container>
    </template>
    <template v-if="$parent.current.lesson.type === '4'">
      <div id="lesson-task" class="lesson-task" v-html="content.markdown"></div>
    </template>
  </div>
  <div v-else class="progress-container contrast">
    <v-container fluid fill-height>
      <v-layout column align-center justify-center>
        <v-progress-circular indeterminate :size="$store.state.progress.size" :width="$store.state.progress.width" v-if="!$store.state.progress.error"></v-progress-circular>
        <div class="error text-center" v-else>!</div>
        <div class="text text-center">{{$store.state.progress.text}}</div>
      </v-layout>
    </v-container>
  </div>
</template>
<script src="./lesson.js"></script>
<style src="./lesson.scss" lang="scss"></style>
