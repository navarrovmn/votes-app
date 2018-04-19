from django.contrib import admin
from . import models


admin.site.register(models.Election)
admin.site.register(models.Candidate)
admin.site.register(models.SimpleVote)
admin.site.register(models.MultiVote)
admin.site.register(models.PriorityVote)
