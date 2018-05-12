from django.urls import path, include

from . import api


lesson_urls = [
    path('lessons/',
         api.MarkdownLessonListAPIView.as_view(),
         name='lesson_list_api'),

    path('lessons/<slug:slug>/',
         api.MarkdownRetrieveUpdateAPIView.as_view(),
         name='lesson_retrieve_update_api'),

    path('videos/',
         api.VideoLessonListAPIView.as_view(),
         name='video_list_api'),

    path('videos/<slug:slug>/',
         api.VideoRetrieveUpdateAPIView.as_view(),
         name='video_retrieve_update_api'),

    path('quizes/',
         api.QuizLessonListAPIView.as_view(),
         name='quiz_list_api'),

    path('quizes/<slug:slug>/',
         api.QuizRetrieveUpdateAPIView.as_view(),
         name='quiz_retrieve_update_api'),
]

api_urls = [
    path('tracks/<slug:track_slug>/workshops/<slug:workshop_slug>/modules/<slug:module_slug>/',
         include(lesson_urls)),

    path('tracks/<slug:track_slug>/workshops/<slug:workshop_slug>/modules/',
         api.ModuleListAPIView.as_view(),
         name='module_liste_api'),

    path('tracks/<slug:track_slug>/workshops/<slug:workshop_slug>/modules/<slug:slug>/',
         api.ModuleRetrieveAPIView.as_view(),
         name='module_retrieve_api'),

    path('tracks/<slug:track_slug>/workshops/',
         api.WorkshopListAPIView.as_view(),
         name='workshops_list_api'),

    path('tracks/<slug:track_slug>/workshops/<slug:slug>',
         api.WorkshopRetrieveAPIView.as_view(),
         name='workshops_retrieve_api'),

    path('tracks/',
         api.TrackListAPIView.as_view(),
         name='tracks_list_api'),

    path('tracks/<slug:slug>/',
         api.TrackRetrieveAPIView.as_view(),
         name='tracks_retrieve_api'),
]

urlpatterns = [
    path('', include(api_urls))
]
