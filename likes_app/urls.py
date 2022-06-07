from django.urls import include, path

from .api.views.router import api_router

urlpatterns = [
    path('api/', include(api_router.urls)),
]
