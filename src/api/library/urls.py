from django.urls import path, include

from . import api


api_urls = [
    # path('tracks/<slug:track_slug>/workshops/<slug:workshop_slug>/modules/<slug:module_slug>/',
    #     include(lesson_urls)),

    # path('tracks/<slug:track_slug>/workshops/<slug:workshop_slug>/modules/',
    #     api.ModuleListAPIView.as_view(),
    #     name='module_list_api'),

    # path('tracks/<slug:track_slug>/workshops/<slug:workshop_slug>/modules/<slug:slug>/',
    #     api.ModuleRetrieveAPIView.as_view(),
    #     name='module_retrieve_api'),

    # path('tracks/<track_slug>/workshops/<workshop_slug>/modules/<module_slug>/lessons/<slug>',
    #    api.BaseLessonRetrieveUpdateAPIView.as_view(),
    #     name='lesson_retrieve_update_api'),

    path('tracks/<track_slug>/workshops/',
         api.WorkshopListAPIView.as_view(),
         name='workshops_list_api'),

    path('tracks/<track_slug>/workshops/<slug>',
         api.WorkshopRetrieveAPIView.as_view(),
         name='workshops_retrieve_api'),

    path('tracks/',
         api.TrackListAPIView.as_view(),
         name='tracks_list_api'),

    path('tracks/<slug>/',
         api.TrackRetrieveAPIView.as_view(),
         name='tracks_retrieve_api'),
]

urlpatterns = [
    path('', include(api_urls))
]
