from django.shortcuts import render
from django.http import HttpResponse


def polls_list(request):
    ctx = {}
    return render(request, 'votes/vote_list.html', ctx)