import pytest
from votes.models import *
from django.contrib.auth.models import User


@pytest.fixture
def simple_election(db):
    election = Election.objects.create(title="Linguagem", kind=Election.KIND_SIMPLE)
    Candidate.objects.create(slug="Python", display_name="Python", election=election)
    Candidate.objects.create(slug="Ruby", display_name="Ruby", election=election)
    return election

@pytest.fixture
def user(db):
    return User.objects.create(first_name="Victor", last_name="Navarro", email="victor@gmail.com")

def test_user_should_votes_only_once(simple_election, user):
    simple_election.vote(user, "Python")
    with pytest.raises(ValueError):
        simple_election.vote(user, "Ruby")

def test_not_vote_unregisteres_cadidate(simple_election, user):
    with pytest.raises(ValueError):
        simple_election.vote(user, "Unknown Language")

def test_user_votes(simple_election, user):
    simple_election.vote(user, "Python")
    assert Candidate.objects.filter(name="Python").votes == 1