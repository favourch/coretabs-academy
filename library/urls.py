from django.urls import path, include

from . import api


api_urls = [
    path('tracks/<slug:track_slug>/workshops/<slug:workshop_slug>/modules/<slug:module_slug>/lessons/<slug:slug>/',
         api.LessonRetrieveUpdateAPIView.as_view(),
         name='lesson_retrieve_api'),

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
