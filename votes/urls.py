from django.urls import path, include
from .viewsets import ElectionViewSet, CandidateViewSet
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"elections", ElectionViewSet)
router.register(r"candidates", CandidateViewSet)

urlpatterns = [
    path('', views.elections_list),
    path('api/', include(router.urls))
]
