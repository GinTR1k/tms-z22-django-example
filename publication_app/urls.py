from django.urls import path

from publication_app.api.views.publications import PostsView
from publication_app.views.auth import AuthView
from publication_app.views.registration import RegistrationView
from publication_app.views.main import MainPageView, PostListView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('registration/', RegistrationView.as_view(), name='reg_page'),
    path('login/', AuthView.as_view(), name='login_page'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('api/posts/', PostsView.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'}), name='api-posts'),
]
