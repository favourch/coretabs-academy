from django.urls import path, include

from . import api


api_urls = [
    path('tracks/<int:track_pk>/workshops/<int:workshop_pk>/modules/<int:module_pk>/lessons/',
         api.LessonListAPIView.as_view(),
         name='lesson_list_api'),

    path('tracks/<int:track_pk>/workshops/<int:workshop_pk>/modules/<int:module_pk>/lessons/<int:lesson_pk>/',
         api.LessonRetrieveAPIView.as_view(),
         name='lesson_retrieve_api'),

    path('tracks/<int:track_pk>/workshops/<int:workshop_pk>/modules/',
         api.ModuleListAPIView.as_view(),
         name='module_liste_api'),

    path('tracks/<int:track_pk>/workshops/<int:workshop_pk>/modules/<int:module_pk>/',
         api.ModuleRetrieveAPIView.as_view(),
         name='module_retrieve_api'),

    path('tracks/<int:track_pk>/workshops/',
         api.WorkshopListAPIView.as_view(),
         name='workshops_list_api'),

    path('tracks/<int:track_pk>/workshops/<int:workshop_pk>',
         api.WorkshopRetrieveAPIView.as_view(),
         name='workshops_retrieve_api'),

    path('tracks/',
         api.TrackListAPIView.as_view(),
         name='tracks_list_api'),

    path('tracks/<int:track_pk>/',
         api.TrackRetrieveAPIView.as_view(),
         name='tracks_retrieve_api'),
]

urlpatterns = [
    path('', include(api_urls))
]
