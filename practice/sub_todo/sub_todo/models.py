"""sub_todo Models."""

from django.db import models


class MainItem(models.Model):
    to_do_category = models.TextField()

    def __str__(self):
        return self.to_do_category

    def __repr__(self):
        return 'MainItem(to_do_category={!r}'.format(self.to_do_category)


class SubItem(models.Model):
    main_item = models.ForeignKey(MainItem)
    task = models.TextField()

    def __str__(self):
        return self.task

    def __repr__(self):
        return 'SubItem(task={!r}'.format(self.task)

