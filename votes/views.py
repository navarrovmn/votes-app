from django.shortcuts import render
from django.http import HttpResponse
from votes.models import Poll


def polls_list(request):
    ctx = dict(
        polls=Poll.objects.all(),
    )
    return render(request, 'votes/vote_list.html', ctx)