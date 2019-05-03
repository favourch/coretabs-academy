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
          <router-link to="/profile/personal-info" replace>
            <v-list-tile>
              <v-list-tile-action>
                <v-icon :color="`grey`">settings</v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title v-html="i18n.personal_info"></v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </router-link>
          <v-divider></v-divider>
          <router-link to="/profile/change-track" replace>
            <v-list-tile>
              <v-list-tile-action>
                <v-icon :color="`grey`">compare_arrows</v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title v-html="i18n.change_track"></v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </router-link>
          <v-divider></v-divider>
          <router-link to="/profile/change-password" replace>
            <v-list-tile>
              <v-list-tile-action>
                <v-icon :color="`grey`">lock</v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title v-html="i18n.change_password"></v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </router-link>
        </v-list>
      </v-navigation-drawer>
      <section id="column-flexed">
        <inner-header-component :title="header"></inner-header-component>
        <div class="content">
          <router-view ></router-view>
        </div>
      </section>
    </section>
  </div>
</template>
<script src="./profile-settings.js"></script>
<style src="./profile-settings.scss" lang="scss"></style>
