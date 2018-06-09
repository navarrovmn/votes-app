from django.shortcuts import render
from django.http import HttpResponse
from votes.models import Election


def elections_list(request, filename):
    ctx = dict(
        elections=Election.objects.all(),
    )
    return render(request, 'votes/vote_list.html', ctx)


def elections_detail(request, id):
    election = Election.objects.get(id=id)
    ctx = dict(
        election=election,
        election_kind=election.kind_name,
        candidates=(
            election.candidates
                .filter(is_active=True)
                .defer('slug')
                .prefetch_related('simplevotes')
        ),
    )
    return render(request, 'votes/vote_detail.html', ctx)
