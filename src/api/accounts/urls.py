from django.urls import path, include
from .views import (
    LoginView, LogoutView, UserDetailsView, PasswordChangeView,
    PasswordResetView, PasswordResetConfirmView, ResendConfirmView,
    RegisterView, VerifyEmailView,
)

urlpatterns = [
    # URLs that do not require a session or valid token
    path('password/reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('login/', LoginView.as_view(), name='login'),
    path('confirmation/', ResendConfirmView.as_view(), name='resend_confirm'),

    # URLs that require a user to be logged in with a valid session / token.
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/', UserDetailsView.as_view(), name='user_details'),
    path('password/change/', PasswordChangeView.as_view(), name='password_change'),

    # Registration Urls
    path('registration/', RegisterView.as_view(), name='registration'),
    path('registration/verify-email/', VerifyEmailView.as_view(), name='verify_email'),

    # Social auth Urls
    path('social/', include('accounts.social.urls')),
]
