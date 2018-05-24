from django.contrib.auth import get_user_model
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from boogie.rest import rest_api

from . import views
from . import models

# Inclui o modelo User na API
rest_api(get_user_model())

urlpatterns = [
    path('', views.elections_list, name='election-list'),
    path('elections/<int:id>/', views.elections_detail, name='election-detail'),
    path('api/', include(rest_api.urls))
]
