from django.urls import path, include

from rest_framework import routers

from .views import MyProfileView, MyProfileProjectsViewSet, ProfileView, CertificateView

router = routers.SimpleRouter()
router.register('ppp', MyProfileProjectsViewSet, base_name='ppp')

urlpatterns = [
    path('profile', MyProfileView.as_view(), name='my_profile'),

    path('profile/projects', MyProfileProjectsViewSet.as_view({'post': 'create'}), name='my_profile_projects'),
    path('profile/projects/<pk>', 
          MyProfileProjectsViewSet.as_view({'patch': 'partial_update',
                                            'delete': 'destroy'}), 
          name='my_profile_projects_update_delete'),

    #path('profile/projects', include((router.urls, 'profiles'), namespace='profiles')),
    path('profiles/<username>', ProfileView.as_view(), name='profile'),
    path('certificates/<uuid>', CertificateView.as_view(), name='certificate'),
]
