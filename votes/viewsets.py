from rest_framework.viewsets import ModelViewSet
from votes.serializers import ElectionSerializer, CandidateSerializer
from votes.models import Election, Candidate

class ElectionViewSet(ModelViewSet):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer

class CandidateViewSet(ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer