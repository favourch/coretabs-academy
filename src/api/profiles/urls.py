from django.urls import path
from .views import ProfileView

urlpatterns = [
    path('<username>', ProfileView.as_view(), name='profile'),
]
