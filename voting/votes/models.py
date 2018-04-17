from django.db import models


class Poll(models.Model):
    KIND_SIMPLE = 0
    KIND_MULTI = 1
    KIND_PRIORITY_LIST = 2
    KIND_CHOICES = [
        (KIND_SIMPLE, 'simple'),
        (KIND_MULTI, 'multi'),
        (KIND_PRIORITY_LIST, 'priority_list'),
    ]
    
    title = models.CharField(max_length=140)
    kind = models.PositiveIntegerField(choices=KIND_CHOICES)

    def vote(self, user, value):
        raise NotImplementedError

    def get_priorities(self, user):
        raise NotImplementedError

    def get_priorities_map(self):
        raise NotImplementedError


class Value(models.Model):
    poll = models.ForeignKey(
        'Poll', 
        on_delete=models.CASCADE,
        related_name='values',
    )
    slug = models.CharField(max_length=20)
    value = models.CharField(max_length=140)


class Vote(models.Model):
    poll = models.ForeignKey(
        'Poll',
        on_delete=models.CASCADE,
        related_name='votes',
    )
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='votes',
    )
    value = models.ForeignKey(
        'Value',
        on_delete=models.CASCADE,
        related_name='votes',
    )
    priority = models.PositiveSmallIntegerField(
        default=0,
    )
