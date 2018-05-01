from django.urls import path, include

from . import api


api_urls = [
    path('lessons/',
         api.LessonListAPIView.as_view(),
         name='lesson_list_create_api'),

    path('lessons/<int:pk>/',
         api.LessonRetrieveAPIView.as_view(),
         name='lesson_retrieve_update_destroy_api'),

    path('modules/',
         api.ModuleListAPIView.as_view(),
         name='module_list_create_api'),

    path('modules/<int:pk>/',
         api.ModuleRetrieveAPIView.as_view(),
         name='module_retrieve_update_destroy_api'),

    path('modules_lessons/',
         api.ModuleLessonListAPIView.as_view(),
         name='module_lesson_list_create_api'),

    path('modules_lessons/<int:pk>/',
         api.ModuleLessonRetrieveAPIView.as_view(),
         name='module_lesson_retrieve_update_destroy_api'),

    path('tracks/',
         api.TrackListAPIView.as_view(),
         name='tracks_list_create_api'),

    path('tracks/<int:pk>/',
         api.TrackRetrieveAPIView.as_view(),
         name='tracks_retrieve_update_destroy_api'),

    path('tracks_modules/',
         api.TrackModuleListAPIView.as_view(),
         name='track_module_list_create_api'),

    path('tracks_modules/<int:pk>/',
         api.TrackModuleRetrieveAPIView.as_view(),
         name='track_module_retrieve_update_destroy_api'),
]

urlpatterns = [
    path('v1/', include(api_urls))
]
