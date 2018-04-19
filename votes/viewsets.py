from rest_framework.viewsets import ModelViewSet
from votes.serializers import ElectionSerializer, CandidateSerializer
from votes.serializers import MultiVoteSerializer, PriorityVoteSerializer
from votes.serializers import SimpleVoteSerializer 
from votes.models import Election, Candidate, SimpleVote, MultiVote, PriorityVote

class ElectionViewSet(ModelViewSet):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer


class CandidateViewSet(ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class SimpleVoteViewSet(ModelViewSet):
    queryset = SimpleVote.objects.all()
    serializer_class = SimpleVoteSerializer


class MultiVoteViewSet(ModelViewSet):
    queryset = MultiVote.objects.all()
    serializer_class = MultiVoteSerializer


class PriorityVoteViewSet(ModelViewSet):
    queryset = PriorityVote.objects.all()
    serializer_class = PriorityVoteSerializer
