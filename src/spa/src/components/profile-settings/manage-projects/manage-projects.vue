<template>
    <div class="manage-projects" v-if="projects">
      <v-container fluid>
        <v-layout row wrap>
          <v-flex d-flex class="mother-container">
            <v-layout row wrap>
              <v-flex xs12>
                <header class="manage-projects__header">
                  <v-btn round id="add-project" class="ma-0" @click="addProject" > <!-- :disabled="waiting" --> 
                    {{ i18n.add_project_btn_text }}
                  </v-btn>
                   <v-dialog
                    v-model="dialog"
                    max-width="500"
                    persistent
                  >
                    <v-card>
                      <div class="pic-container">
                        <img v-if="project_img" :src="project_img" :alt="project_name">

                        <div class="add-image-btn" title="إضافة صورة للمشروع" v-if="!project_img">
                          <label for="file_uploader" class="cursor-pointer">
 
                            <v-icon>photo_camera</v-icon>
                            <input @change="previewImage($event)" v-show="false" name="project-img" type="file" id="file_uploader" accept="image/*"/>

                            <p>{{ i18n.add_project_img_label }}</p>
                          </label>
                        </div>

                        <label for="file_uploader" class="leave cursor-pointer" v-else>
                          <v-icon small>edit</v-icon>
                          <input @change="previewImage($event)" v-show="false" name="avatar" type="file" id="file_uploader" accept="image/*"/>
                        </label>
                      </div>

                      <div class="form-container">
                        <v-form ref="form" lazy-validation>
                          <v-alert type="success" v-model="alert.success" v-text="alert.message"></v-alert>
                          <v-alert type="error" v-model="alert.error" v-text="alert.message"></v-alert>
                          <v-text-field dir="auto" :label="form.projectname_label" v-model="project_name" @keyup.enter="submit" :rules="pnRules" required></v-text-field>
                          <v-text-field dir="auto" prepend-icon="fab fa-github" :label="form.repo_link" v-model="repo_link" @keyup.enter="submit"></v-text-field>
                          <v-text-field dir="auto" prepend-icon="fas fa-globe" :label="form.demo_link" v-model="demo_link" @keyup.enter="submit"></v-text-field>
                        </v-form>
                      </div>
                      <v-card-actions class="dialog-footer">
                        <v-btn round class="yes" :disabled="!valid || waiting" @click="submit">
                          <v-progress-circular indeterminate size="24" class="ml-2" v-if="waiting"></v-progress-circular>
                          {{ i18n.submit_btn_text }}
                        </v-btn>
                        <v-btn round class="no" @click="dialog = false" v-if="!waiting"> 
                          {{ i18n.close_btn_text }}
                        </v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                  
                </header>

                <v-list v-if="projects.length > 0">
                  <v-list-tile
                    v-for="(project, index) in projects"
                    :key="index"
                    @click="editProject(project.id)"
                  >
                    <v-list-tile-content>
                      <v-list-tile-title v-html="project.description"></v-list-tile-title>
                    </v-list-tile-content>

                    <v-list-tile-action>
                      <v-btn icon ripple @click.stop="editProject(project.id)">
                        <v-icon>edit</v-icon>
                      </v-btn>

                      <v-btn icon ripple @click.stop="openDeleteDialog(project.id)">
                        <v-icon>delete_outline</v-icon>
                      </v-btn>
                    </v-list-tile-action>
                  </v-list-tile>
                </v-list>

                <div id="emptyState" v-else>
                  {{ i18n.empty_state }}
                </div>

                <v-dialog v-model="deleteDialog" content-class="delete-dialog" max-width="500">
                  <v-card>
                    <div class="dialog-body">
                      <v-card-title class="delete-dialog__title pa-0 headline">{{ i18n.delete_project_title }}</v-card-title>

                      <v-card-text class="pa-0">
                        {{ i18n.delete_project_message }} <strong>{{ project_name }}</strong>
                      </v-card-text>
                    </div>

                    <v-card-actions class="dialog-footer">
                      <v-btn round class="no" @click="deleteDialog = false">
                        {{ i18n.close_btn_text }}
                      </v-btn>

                      <v-btn round class="yes delete-btn" @click="deleteProject" :disabled="waiting">
                        <v-progress-circular indeterminate size="24" class="ml-2" v-if="waiting"></v-progress-circular>                        
                        {{ i18n.delete_btn_text }}
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
              </v-flex>
            </v-layout>
            </v-flex>
        </v-layout>
      </v-container>
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

<script src="./manage-projects.js"></script>
<style src="./manage-projects.scss" lang="scss"></style>