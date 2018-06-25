<template>
<div v-if="loading" class="progress-container" :class="$store.state.progress.classList">
  <v-container fluid fill-height>
    <v-layout column align-center justify-center>
      <v-progress-circular indeterminate :size="$store.state.progress.size" :width="$store.state.progress.width" ></v-progress-circular>
      <div class="progress-text text-center">{{$store.state.progress.pageText}}...</div>
    </v-layout>
  </v-container>
</div>
</template>
<script src="./loading.js"></script>
<style src="./loading.scss" lang="scss" scoped></style>
