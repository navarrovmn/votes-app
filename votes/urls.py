from django.urls import path, include
from .viewsets import PollViewSet, VoteViewSet, ValueViewSet
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"polls", PollViewSet)
router.register(r"vote", VoteViewSet)
router.register(r"value", ValueViewSet)

urlpatterns = [
    path('', views.polls_list),
    path('api/', include(router.urls))
]
