<template>
  <div class="settings">
    <NavigatorDrawerComponent />
    <section id="row-flexed">
      <v-navigation-drawer id="sidenav" :right="drawer.isRight" v-model="drawer.isOpen" :width="$store.state.css.workshops.drawerWidth"
        hide-overlay>
        <v-toolbar flat>
          <v-btn @click="$router.go(-1)" icon>
            <v-icon>keyboard_arrow_right</v-icon>
          </v-btn>
          <v-toolbar-title v-html="i18n.settings"></v-toolbar-title>
        </v-toolbar>
        <v-list class="py-0">
          <template v-for="(navItem,i) in navDrawer">
            <router-link :to="navItem.route" replace :key="i">
              <v-list-tile  @click="setCurrentRoute(navItem.name)" :class="{'stepper-item__active' : currentRoute == navItem.name}">
                <v-list-tile-action>
                  <v-icon :color="`grey`">{{navItem.icon}}</v-icon>
                </v-list-tile-action>
                <v-list-tile-content>
                  <v-list-tile-title v-html="navItem.text"></v-list-tile-title>
                </v-list-tile-content>
              </v-list-tile>
            </router-link>
            <v-divider :key="i"></v-divider>
          </template>
        </v-list>
      </v-navigation-drawer>
      <section id="column-flexed">
        <inner-header-component :title="header"></inner-header-component>
        <div class="content" :style="{ height: height + 'px' }" v-resize="onResize">
          <router-view ></router-view>
        </div>
      </section>
    </section>
  </div>
</template>
<script src="./profile-settings.js"></script>
<style src="./profile-settings.scss" lang="scss"></style>
