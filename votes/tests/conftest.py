import pytest
from votes.models import * 
from django.contrib.auth.models import User


@pytest.fixture
def simple_election(db):
    election = Election.objects.create(title="Linguagem", kind=Election.KIND_SIMPLE)
    Candidate.objects.create(slug="python", display_name="Python", election=election)
    Candidate.objects.create(slug="ruby", display_name="Ruby", election=election)
    return election

@pytest.fixture
def user(db):
    return User.objects.create(first_name="Victor", last_name="Navarro", email="victor@gmail.com")
