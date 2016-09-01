"""sub_todo Logic."""

from . import models


def create_new_main_item(name):
    new_main_task = models.MainItem(name=name)
    new_main_task.save()


def create_sub_task(task, main_item):
    new_sub_task = models.SubItem(
        main_item=main_item,
        task=task
    )
    new_sub_task.save()


def get_all_tasks():
    return models.MainItem.objects.all()

def get_main_item_by_id(main_item):
    return models.MainItem.objects.get(id__exact=main_item)


def get_sub_item_by_id(sub_item_id):
     return models.SubItem.objects.get(id__exact=sub_item_id)


def delete_sub_item(sub_item_id, main_item_id):
    sub_item = get_sub_item_by_id(sub_item_id)
    sub_item.delete()
    main_item = get_main_item_by_id(main_item_id)
    if len(main_item.sub_items.all()) == 0:
        main_item.delete()


