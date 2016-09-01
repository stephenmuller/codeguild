"""sub_todo Admin Configuration."""

from django.contrib import admin
from . import models

admin.site.register(models.MainItem)
admin.site.register(models.SubItem)