from django.urls import reverse
from django.db import models
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.db.models import Q, F
from django.utils.translation import ugettext_lazy as _
from boogie.rest import rest_api


@rest_api()
class Election(models.Model):
    """
    Represents an election.

    Elections can be created from a 
    """

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
    kind_name = property(lambda self: self.kind_display())

    @property
    def candidates_map(self):
        return {x.slug: x.display_name for x in self.candidates}

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {'id': self.id}
        return reverse('election-detail', kwargs=kwargs)

    def set_candidates(self, map):
        """
        Register all candidates of an election from a map of candidate slugs
        to their respective display names.
        """
        if self.id is None:
            self.save()
        candidates = []
        for slug, name in map.items():
            elem, _ = self.candidates.get_or_create(slug=slug, display_name=name)
            candidates.append(elem)
        return candidate
 
    def vote(self, user, candidate, priority=0):
        """
        Cast a vote from a given user to a candidate.

        Candidate can be either a Candidate instance or a string with the 
        candidate slug.
        """
        # Check candidate
        if isinstance(candidate, str):
            try:
                candidate = self.candidates.get(slug=candidate)
            except Candidate.DoesNotExist:
                raise ValueError(f'invalid candidate: {candidate}')

        # Create vote object
        if self.kind == self.KIND_SIMPLE:
            try:
                return self.simplevotes.create(user=user, candidate=candidate)
            except IntegrityError:
                raise ValueError('user already voted')
        elif self.kind == self.KIND_MULTI:
            obj, _ = self.multivotes.get_or_create(user=user, 
                                                   candidate=candidate)
            return obj
        elif self.kind == self.KIND_PRIORITY_LIST:
            create = PriorityVote.objects.create
            return self.priorityvotes.create(user=user, candidate=candidate,
                                             priority=priority)
        else:
            raise ValueError(f'invalid votation type: {self.kind}')

    def get_priorities(self, user):
        raise NotImplementedError

    def get_priorities_map(self):
        raise NotImplementedError


@rest_api()
class Candidate(models.Model):
    """
    Represents a candidate in a election.
    """
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
        elif self.election.kind == Election.KIND_MULTI:
            return self.multivotes.count()
        elif self.election.kind == Election.KIND_PRIORITY_LIST:
            return self.priorityvotes.count()
        else:
            raise NotImplementedError


class BaseVote(models.Model):
    class Meta:
        abstract = True

    election = models.ForeignKey(
        'Election',
        on_delete=models.CASCADE,
        related_name='%(class)ss',
    )
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='%(class)ss',
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


@rest_api()
class SimpleVote(BaseVote):
    class Meta:
        unique_together = [('election', 'user')]


@rest_api()
class MultiVote(BaseVote):
    class Meta:
        unique_together = [('election', 'candidate'), ('candidate', 'user')]


@rest_api()
class PriorityVote(BaseVote):
    priority = models.PositiveSmallIntegerField(
        default=0,
    )

    class Meta:
        unique_together = [('election', 'candidate'), ('candidate', 'user')]
