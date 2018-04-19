import os
import sys


def make_users():
    from django.contrib.auth.models import User

    admin, _ = User.objects.update_or_create(first_name='maurice', last_name='moss', id=1,
        username='admin', email='admin@admin.com', is_active=True, is_staff=True, is_superuser=True)
    admin.set_password('admin')
    admin.save()

    return dict(admin=admin)


def make_language_election(users):
    from votes.models import Election, Candidate, SimpleVote, MultiVote, PriorityVote

    election = Election.objects.create(title='languages', kind=Election.KIND_SIMPLE)


def make_all():
    users = make_users()
    make_language_election(users)
