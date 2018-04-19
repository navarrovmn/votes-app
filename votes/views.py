from django.shortcuts import render
from django.http import HttpResponse
from votes.models import Election


def polls_list(request):
    ctx = dict(
        elections=Election.objects.all(),
    )
    return render(request, 'votes/vote_list.html', ctx)
