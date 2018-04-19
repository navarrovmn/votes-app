from rest_framework.serializers import ModelSerializer
from votes.models import Poll, Value, Vote

class PollSerializer(ModelSerializer):
    class Meta:
        model = Poll
        fields = ["id", "title", "kind"]

class ValueSerializer(ModelSerializer):
    class Meta:
        model = Value
        fields = ["id", "poll", "slug", "value"]

class VoteSerializer(ModelSerializer):
    class Meta:
        model = Vote
        fields = ["id", "poll", "user", "value"]