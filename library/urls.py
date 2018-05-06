from django.urls import path, include

from . import api


api_urls = [
    path('tracks/<int:pk>/workshops/modules/lessons/',
         api.LessonListAPIView.as_view(),
         name='lesson_list_api'),

    path('tracks/<int:pk>/workshops/modules/lessons/<int:pk>/',
         api.LessonRetrieveAPIView.as_view(),
         name='lesson_retrieve_api'),

    path('tracks/<int:pk>/workshops/modules/',
         api.ModuleListAPIView.as_view(),
         name='module_liste_api'),

    path('tracks/<int:pk>/workshops/modules/<int:pk>/',
         api.ModuleRetrieveAPIView.as_view(),
         name='module_retrieve_api'),

    path('tracks/<int:pk>/workshops/',
         api.WorkshopListAPIView.as_view(),
         name='workshops_list_api'),

    path('tracks/<int:pk>/workshops/<int:pk>',
         api.WorkshopRetrieveAPIView.as_view(),
         name='workshops_retrieve_api'),

    path('tracks/',
         api.TrackListAPIView.as_view(),
         name='tracks_list_api'),

    path('tracks/<int:pk>/',
         api.TrackRetrieveAPIView.as_view(),
         name='tracks_retrieve_api'),
]

urlpatterns = [
    path('v1/', include(api_urls))
]
