import pytest
from votes.models import *


def test_user_should_vote_only_once(simple_election, user):
    simple_election.vote(user, "python")
    with pytest.raises(ValueError):
        simple_election.vote(user, "ruby")

def test_cannot_vote_on_unregistered_cadidate(simple_election, user):
    with pytest.raises(ValueError):
        simple_election.vote(user, "unknown language")

def test_user_can_vote(simple_election, user):
    simple_election.vote(user, "python")
    assert Candidate.objects.get(slug="python").simplevotes.count() == 1