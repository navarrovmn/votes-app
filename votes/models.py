from django.urls import reverse
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Q, F
from django.utils.translation import ugettext_lazy as _


class Election(models.Model):
    KIND_SIMPLE = 0
    KIND_MULTI = 1
    KIND_PRIORITY_LIST = 2
    KIND_CHOICES = [
        (KIND_SIMPLE, _('Simple')),
        (KIND_MULTI, _('Multi')),
        (KIND_PRIORITY_LIST, _('Priority list')),
    ]
    KIND_MAP = dict(KIND_CHOICES)

    title = models.CharField(max_length=140)
    kind = models.PositiveIntegerField(choices=KIND_CHOICES)
    kind_name = property(lambda self: self.KIND_MAP[self.kind])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {'id': self.id}
        return reverse('election-detail', kwargs=kwargs)

    def vote(self, user, candidate):
        raise NotImplementedError

    def get_priorities(self, user):
        raise NotImplementedError

    def get_priorities_map(self):
        raise NotImplementedError


class Candidate(models.Model):
    election = models.ForeignKey(
        'Election',
        on_delete=models.CASCADE,
        related_name='candidates',
    )
    slug = models.CharField(max_length=20)
    display_name = models.CharField(max_length=140)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.display_name

    class Meta:
        unique_together = [('election', 'slug')]

    def get_num_votes(self):
        if self.election.kind == Election.KIND_SIMPLE:
            return self.simplevotes.count()
        else:
            raise NotImplementedError


class BaseVote(models.Model):
    class Meta:
        abstract = True

    election = models.ForeignKey(
        'Election',
        on_delete=models.CASCADE,
        related_name='%(class)s',
    )
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='%(class)s',
    )
    candidate = models.ForeignKey(
        'Candidate',
        on_delete=models.CASCADE,
        related_name='%(class)ss',
    )

    def __str__(self):
        return self.election.title + " - " + self.candidate.display_name

    def clean(self):
        if self.candidate.election_id != self.election_id:
            raise ValidationError(
                "Opção obscura não válida para votações ortodoxas")


class SimpleVote(BaseVote):
    class Meta:
        unique_together = [('election', 'user')]


class MultiVote(BaseVote):
    class Meta:
        unique_together = [('election', 'candidate'), ('candidate', 'user')]


class PriorityVote(BaseVote):
    priority = models.PositiveSmallIntegerField(
        default=0,
    )

    class Meta:
        unique_together = [('election', 'candidate'), ('candidate', 'user')]
