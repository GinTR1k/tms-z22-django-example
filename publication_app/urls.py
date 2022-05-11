from django.urls import path

from publication_app.views.auth import AuthView
from publication_app.views.registration import RegistrationView
from publication_app.views.main import MainPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('registration', RegistrationView.as_view(), name='reg_page'),
    path('login', AuthView.as_view(), name='login_page'),
]
