from django.contrib import admin
from . import models


class CanditatesAdmin(admin.TabularInline):
    model = models.Candidate


class ElectionAdmin(admin.ModelAdmin):
    fields = ['title', 'kind']
    inlines = [CanditatesAdmin]


admin.site.register(models.Election, ElectionAdmin)
