from rest_framework.serializers import ModelSerializer
from votes.models import Election, Candidate, BaseVote

class ElectionSerializer(ModelSerializer):
    class Meta:
        model = Election
        fields = ["id", "title", "kind"]

class CandidateSerializer(ModelSerializer):
    class Meta:
        model = Candidate
        fields = ["id", "election", "slug", "display_name"]
