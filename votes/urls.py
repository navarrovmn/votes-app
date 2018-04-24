from django.urls import path, include
from .viewsets import ElectionViewSet, CandidateViewSet, SimpleVoteViewSet
from .viewsets import MultiVoteViewSet, PriorityVoteViewSet
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"elections", ElectionViewSet)
router.register(r"candidates", CandidateViewSet)
router.register(r"multi", MultiVoteViewSet)
router.register(r"simple", SimpleVoteViewSet)
router.register(r"priority", PriorityVoteViewSet)


urlpatterns = [
    path('', views.elections_list, name='election-list'),
    path('elections/<int:id>/', views.elections_detail, name='election-detail'),
    path('api/', include(router.urls))
]
