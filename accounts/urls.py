from django.urls import path
from accounts.views import ProfileView, LoginView, LogoutView, RegistrationView, CustomChangePasswordView

app_name = 'accounts'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('registration-done/', LogoutView.as_view(), name='registration-done'),
    path('change-password/', CustomChangePasswordView.as_view(), name='change-password'),
]
