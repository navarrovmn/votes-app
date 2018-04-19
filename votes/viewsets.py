from rest_framework.viewsets import ModelViewSet
from votes.serializers import PollSerializer, VoteSerializer, ValueSerializer
from votes.models import Poll, Vote, Value

class PollViewSet(ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class VoteViewSet(ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

class ValueViewSet(ModelViewSet):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer