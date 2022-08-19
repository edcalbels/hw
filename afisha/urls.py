"""afisha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movie_app import views
from profile_app import views as user_views
from . import swagger

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.DirectorAPIViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),
    path('api/v1/movies/', views.MovieAPIViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),
    path('api/v1/reviews/', views.ReviewAPIViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),
    path('api/v1/directors/<int:pk>/', views.DirectorAPIViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    })),
    path('api/v1/movies/<int:pk>/', views.MovieAPIViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    })),
    path('api/v1/reviews/<int:pk>/', views.ReviewAPIViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    })),
    path('api/v1/movies/reviews/', views.MovieReviewAPIViewSet.as_view({
        'get': 'list'
    })),
    path('api/v1/authorization/', user_views.AuthorizationAPIView.as_view()),
    path('api/v1/registration/', user_views.RegistrationAPIView.as_view()),
]

urlpatterns += swagger.urlpatterns