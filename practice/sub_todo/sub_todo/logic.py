"""sub_todo Logic."""

from . import models
from . import views
from . import urls



def get_all_main_tasks():
    return models.MainItem.objects.all()