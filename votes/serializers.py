from rest_framework.serializers import ModelSerializer
from votes.models import Election, Candidate, SimpleVote, MultiVote, PriorityVote

class ElectionSerializer(ModelSerializer):
    class Meta:
        model = Election
        fields = ["id", "title", "kind"]

class CandidateSerializer(ModelSerializer):
    class Meta:
        model = Candidate
        fields = ["id", "election", "slug", "display_name"]

class SimpleVoteSerializer(ModelSerializer):
    class Meta:
        model = SimpleVote
        fields = ["election", "user", "candidate"]
        

class MultiVoteSerializer(ModelSerializer):
    class Meta:
        model = MultiVote
        fields = ["election", "user", "candidate"]

class PriorityVoteSerializer(ModelSerializer):
    class Meta:
        model = PriorityVote
        fields = ["election", "user", "candidate", "priority"]