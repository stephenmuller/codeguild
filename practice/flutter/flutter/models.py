"""flutter Models."""

from django.db import models
import datetime
from django.db.models import Q
from django.utils import timezone

class Flut(models.Model):
    text = models.TextField()
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """

        >>> str(Flut(text='text'))
        'text'
        """
        return self.text

    def __repr__(self):
        r"""

        >>> a = Flut(text='test', time='datetime.datetime(2016, 9, 13, 17, 42, 46, 735079, tzinfo=<UTC>)')
        >>> a
        Flut(text='test', time='datetime.datetime(2016, 9, 13, 17, 42, 46, 735079, tzinfo=<UTC>)')
        """
        return 'Flut(text={!r}, time={!r})'.format(self.text, self.time)



